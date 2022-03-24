"""This test the homepage"""

def test_request_main_menu_links(client):
    """This tests the navigation bar and ensures every page is there."""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a class="nav-link" href="/Git">Git</a>' in response.data
    assert b'<a class="nav-link" href="/Docker">Docker</a>' in response.data
    assert b'<a class="nav-link" href="/Python_Flask">Python/Flask</a>' in response.data
    assert b'<a class="nav-link" href="/Continuous_Integration_and_Deployment">CICD</a>' in response.data
    assert b'<a class="nav-link" href="/Pylint">Pylint</a>' in response.data
    assert b'<a class="nav-link" href="/Arrange_Act_Assert_Testing">AAA</a>' in response.data
    assert b'<a class="nav-link" href="/Object_Oriented_Programming">OOP</a>' in response.data
    assert b'<a class="nav-link" href="/Solid">SOLID</a>' in response.data

def test_request_index(client):
    """This ensures that the Index page gets the correct HTML response of status code 200"""
    response = client.get("/")
    assert response.status_code == 200

def test_request_git_page(client):
    """This ensures that the Git page gets the correct HTML response of status code 200"""
    response = client.get("/Git")
    assert response.status_code == 200

def test_request_docker_page(client):
    """This ensures that the Docker page gets the correct HTML response of status code 200"""
    response = client.get("/Docker")
    assert response.status_code == 200

def test_request_python_and_flask_page(client):
    """This ensures that the Python/Flask page gets the correct HTML response of status code 200"""
    response = client.get("/Python_Flask")
    assert response.status_code == 200

def test_request_CICD_page(client):
    """This ensures that the CICD page gets the correct HTML response of status code 200"""
    response = client.get("/Continuous_Integration_and_Deployment")
    assert response.status_code == 200

def test_request_Pylint_page(client):
    """This ensures that the Pylint page gets the correct HTML response of status code 200"""
    response = client.get("/Pylint")
    assert response.status_code == 200

def test_request_AAA_page(client):
    """This ensures that the AAA page gets the correct HTML response of status code 200"""
    response = client.get("/Arrange_Act_Assert_Testing")
    assert response.status_code == 200

def test_request_OOP_page(client):
    """This ensures that the OOP page gets the correct HTML response of status code 200"""
    response = client.get("/Object_Oriented_Programming")
    assert response.status_code == 200

def test_request_SOLID_page(client):
    """This ensures that the SOLID page gets the correct HTML response of status code 200"""
    response = client.get("/Solid")
    assert response.status_code == 200

def test_request_page_not_found(client):
    """This ensures that a page that doesn't exist gets the correct HTML response of status code 404"""
    response = client.get("/page1010")
    assert response.status_code == 404