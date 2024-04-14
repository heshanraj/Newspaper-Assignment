from ..fixtures import app, client, agency

def test_list_all_subscribers(client, agency):
    # send request
    response = client.get("/subscriber/")


    assert response.status_code == 200


    parsed = response.get_json()
    assert len(parsed["subscriber"]) == len(agency.subscribers)

def test_add_subscriber(client, agency):
    sub_count_before = len(agency.subscribers)

    # act
    response = client.post("/subscriber/",
                           json={
                               "subname": "Simpsons Subscriber",
                               "subaddy": "Springfield",
                                "sub_id": 90,
                                "specialissues": [],
                                "deliveredissues": [],
                                "newspaper": []

                           })
    assert response.status_code == 200
    # verify
    assert len(agency.subscribers) == sub_count_before + 1

    parsed = response.get_json()
    sub_response = parsed["subscriber"]


    assert sub_response["subname"] == "Simpsons Subscriber"
    assert sub_response["subaddy"] == "Springfield"

def test_get_subscriber_info(client, agency ):

    # Add a new subscriber
    response = client.post("/subscriber/",
                           json={
                               "subname": "Simpsons Subscriber",
                               "subaddy": "Springfield",
                               "sub_id": 90,
                               "specialissues": [],
                               "deliveredissues": [],
                               "newspaper": []
                           })

    assert response.status_code == 200

    parsed = response.get_json()
    sub_id = parsed["subscriber"]["sub_id"]
    response2 = client.get(f"/subscriber/{sub_id}")
    assert response2.status_code == 200
    parsed = response2.get_json()
    assert parsed["subscriber"]["subname"] == "Simpsons Subscriber"
    assert parsed["subscriber"]["subaddy"] == "Springfield"

def test_remove_subscriber(client, agency):
    sub_count_before = len(agency.subscribers)

    # Add a new subscriber
    response = client.post("/subscriber/",
                           json={
                               "subname": "Simpsons Subscriber",
                               "subaddy": "Springfield",
                               "sub_id": 90,
                               "specialissues": [],
                               "deliveredissues": [],
                               "newspaper": []
                           })

    assert response.status_code == 200


    response = client.get("/subscriber/")

    # Test status code
    assert response.status_code == 200


    parsed = response.get_json()
    assert len(parsed["subscriber"]) == sub_count_before + 1
