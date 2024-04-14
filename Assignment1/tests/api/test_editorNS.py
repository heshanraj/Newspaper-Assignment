from ..fixtures import app, client, agency


def test_add_editor(client, agency):
    before = len(agency.editors)
    # act
    response = client.post("/editor/",
                           json={
                               "editorname": "Simpsons Editor",
                               "editoraddress": "Springfield",
                           })
    assert response.status_code == 200

    assert len(agency.editors) == before + 1

    parsed = response.get_json()
    editor_response = parsed["editor"]


    assert editor_response["editorname"] == "Simpsons Editor"
    assert editor_response["editoraddress"] == "Springfield"



def test_list_all_editors(client, agency):

    response = client.get("/editor/")


    assert response.status_code == 200


    parsed = response.get_json()
    assert len(parsed["editor"]) == len(agency.editors)


def test_get_editor_info(client, agency ):
    editor_count_before = len(agency.editors)

    response = client.post("/editor/",
                           json={
                               "editorname": "Simpsons Editor",
                               "editoraddress": "Springfield",
                           })

    assert response.status_code == 200


    response = client.get("/editor/")


    assert response.status_code == 200


    parsed = response.get_json()
    assert len(parsed["editor"]) == editor_count_before + 1
    assert parsed["editor"][0]["editorname"] == "Simpsons Editor"
    assert parsed["editor"][0]["editoraddress"] == "Springfield"


def test_update_editor_info(client, agency ):
    editor_count_before = len(agency.editors)


    response = client.post("/editor/",
                           json={
                               "editorname": "Simpsons Editor",
                               "editoraddress": "Springfield",
                           })

    assert response.status_code == 200

    parsed = response.get_json()
    editor_id = parsed["editor"]["editor_id"]


    response = client.post(f"/editor/{editor_id}",
                           json={
                               "editorname": "Simpsons Editor 2",
                               "editoraddress": "Springfield 2",
                           })

    assert response.status_code == 200


    response = client.get("/editor/")


    assert response.status_code == 200


    parsed = response.get_json()
    assert len(parsed["editor"]) == editor_count_before + 1
    assert parsed["editor"][0]["editorname"] == "Simpsons Editor 2"
    assert parsed["editor"][0]["editoraddress"] == "Springfield 2"


def test_delete_editor(client, agency):
    editor_count_before = len(agency.editors)


    response = client.post("/editor/",
                           json={
                               "editorname": "Simpsons Editor",
                               "editoraddress": "Springfield",
                           })

    assert response.status_code == 200

    parsed = response.get_json()
    editor_id = parsed["editor"]["editor_id"]


    response = client.delete(f"/editor/{editor_id}",
                           json={
                               "editorname": "Simpsons Editor",
                               "editoraddress": "Springfield",
                           })

    assert response.status_code == 200
    assert len(agency.editors) == editor_count_before


