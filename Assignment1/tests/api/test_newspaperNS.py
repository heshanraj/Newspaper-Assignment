# import the fixtures (this is necessary!)
from ..fixtures import app, client, agency

def test_get_newspaper_should_list_all_papers(client, agency):
    # send request
    response = client.get("/newspaper/")

    # test status code
    assert response.status_code == 200


    parsed = response.get_json()
    assert len(parsed["newspapers"]) == len(agency.newspapers)


def test_add_newspaper(client, agency):
    # prepare
    paper_count_before = len(agency.newspapers)

    # act
    response = client.post("/newspaper/",
                           json={
                               "name": "Simpsons Comic",
                               "frequency": 7,
                               "price": 3.14
                           })
    assert response.status_code == 200
    # verify

    assert len(agency.newspapers) == paper_count_before + 1

    parsed = response.get_json()
    paper_response = parsed["newspaper"]


    assert paper_response["name"] == "Simpsons Comic"
    assert paper_response["frequency"] == 7
    assert paper_response["price"] == 3.14

def test_get_newspaper_info(client, agency ):
    paper_count_before = len(agency.newspapers)

    # Add a new newspaper
    response = client.post("/newspaper/",
                           json={
                               "name": "Simpsons Comic",
                               "frequency": 7,
                               "price": 3.14
                           })

    assert response.status_code == 200


    response = client.get("/newspaper/")


    assert response.status_code == 200


    parsed = response.get_json()
    assert len(parsed["newspapers"]) == paper_count_before + 1


    paper_response = parsed["newspapers"][-1]
    assert paper_response["name"] == "Simpsons Comic"
    assert paper_response["frequency"] == 7
    assert paper_response["price"] == 3.14

def test_update_newspaper(client, agency):
    # Add a new newspaper
    response = client.post("/newspaper/",
                           json={
                               "name": "Simpsons Comic",
                               "frequency": 7,
                               "price": 3.14
                           })

    assert response.status_code == 200


    parsed = response.get_json()
    newspaper_id = parsed["newspaper"]["paper_id"]


    updated_data = {
        "name": "Newspaper Updated",
        "frequency": 5,
        "price": 4.99
    }

    response = client.post(f"/newspaper/{newspaper_id}", json=updated_data)


    print(f"/newspaper/{newspaper_id}/")
    assert response.status_code == 200


    response = client.get(f"/newspaper/{newspaper_id}")


    assert response.status_code == 200


    parsed = response.get_json()
    assert parsed["newspaper"]["name"] == "Newspaper Updated"
    assert parsed["newspaper"]["frequency"] == 5
    assert parsed["newspaper"]["price"] == 4.99


def test_delete_newspaper(client, agency):
    response = client.post("/newspaper/", json={
        "name": "Simpsons Comic",
        "frequency": 7,
        "price": 3.14
    })

    parse = response.get_json()
    paper_id = parse["newspaper"]["paper_id"]
    response = client.post("/newspaper/", json={
        "name": "Simpsons Comic",
        "frequency": 7,
        "price": 3.14})

    before = len(agency.newspapers)

    response = client.delete(f"/newspaper/{paper_id}")
    assert response.status_code == 200
    assert len(agency.newspapers) == before - 1


def test_add_issue(client, agency):

    response = client.post("/newspaper/", json={
        "name": "Simpsons Comic",
        "frequency": 7,
        "price": 3.14
    })
    assert response.status_code == 200
    parse = response.get_json()
    newspaper_id = parse["newspaper"]["paper_id"]


    response1 = client.post(f"/newspaper/{newspaper_id}/issue", json={
        "releasedate": "2021-01-01",
        "price": 3.14,
        "pagenumber": 999,
        'released': False,
        'subscriber': []
    })
    assert response1.status_code == 200
    parse = response1.get_json()


    paper = agency.get_newspaper(newspaper_id)


    assert parse["issue"]["releasedate"] == "2021-01-01"
    assert parse["issue"]["price"] == 3.14
    assert parse["issue"]["issue_id"] == paper.issues[-1].issue_id
    assert parse["issue"]["paper_id"] == paper.paper_id

def test_get_issue(client, agency):
    response = client.post("/newspaper/", json={
        "name": "Simpsons Comic",
        "frequency": 7,
        "price": 3.14
    })
    assert response.status_code == 200
    parse = response.get_json()
    newspaper_id = parse["newspaper"]["paper_id"]
    response = client.get(f"/newspaper/{newspaper_id}/issue")
    assert response.status_code == 200
    parse = response.get_json()
    assert len(parse["issue"]) == 0








