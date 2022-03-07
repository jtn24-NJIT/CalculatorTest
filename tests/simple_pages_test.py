"""This test the homepage"""

def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a class="nav-link" href="/Git">Git</a>' in response.data
    assert b'<a class="nav-link" href="/Docker">Docker</a>' in response.data
    assert b'<a class="nav-link" href="/Python_Flask">Python/Flask</a>' in response.data
    assert b'<a class="nav-link" href="/Continuous_Integration_and_Deployment">Continuous Integration and Deployment</a>' in response.data

def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    # assert b"Index Page." in response.data

def test_request_page1(client):
    """This makes the index page"""
    response = client.get("/Git")
    assert response.status_code == 200
    # assert b"Git Page" in response.data

def test_request_page2(client):
    """This makes the index page"""
    response = client.get("/Docker")
    assert response.status_code == 200
    # assert b"Docker Page check" in response.data

def test_request_page3(client):
    """This makes the index page"""
    response = client.get("/Python_Flask")
    assert response.status_code == 200
    # assert b"Python/Flask Page" in response.data

def test_request_page4(client):
    """This makes the index page"""
    response = client.get("/Continuous_Integration_and_Deployment")
    assert response.status_code == 200
    # assert b"Continuous Integration and Deployment Page" in response.data

def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/page5")
    assert response.status_code == 404