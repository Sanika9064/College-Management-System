from app import app

def test_home_page():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200


def test_add_feedback_get():
    client = app.test_client()
    response = client.get('/add_feedback')
    assert response.status_code == 200


def test_add_course_get():
    client = app.test_client()
    response = client.get('/add_course')
    assert response.status_code == 200


def test_add_enrollment_get():
    client = app.test_client()
    response = client.get('/add_enrollment')
    assert response.status_code == 200