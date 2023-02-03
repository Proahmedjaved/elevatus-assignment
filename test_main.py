from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_mongo_connection():
    response = client.get("/mongo")
    assert response.status_code == 200
    assert response.json() == {"message": "MongoDB Connected"}


def test_add_user():
    response = client.post("/user", json={
        "first_name": "test",
        "last_name": "test", 
        "email": "test@email.com",
        "password": "test"
    })
    assert response.status_code == 200
    global user_id
    user_id = response.json().get("uuid")



def test_user_login():
    # login user in form of email and password
    # login works with email and password and Oauth2PasswordRequestForm
    response = client.post("/login", data={
        "username": "test@email.com",
        "password": "test"
    })
    assert response.status_code == 200

    global access_token
    access_token = response.json().get("access_token")

def test_not_authorized():
    response = client.get(
        f"/user/{user_id}"
        )
    assert response.status_code == 401


def test_create_candidate():
    response = client.post(
        "/candidate",
        json={
            "first_name": "test",
            "last_name": "test", 
            "email": "test@email.com",
            "career_level": "Junior",
            "job_major": "Computer Science",
            "years_of_experience": 1,
            "degree_type": "Bachelor",
            "skills": ["Python", "Django"],
            "nationality": "Egyptian",
            "city": "Cairo",
            "salary": 1000,
            "gender": "MALE"
        },
        headers={"Authorization": f"Bearer {access_token}"}
        )
    assert response.status_code == 200

    global candidate_id
    candidate_id = response.json().get("uuid")

def test_get_candidate():
    response = client.get(
        f"/candidate/{candidate_id}",
        headers={"Authorization": f"Bearer {access_token}"
    }
    )
    assert response.status_code == 200

def test_update_candidate():
    response = client.patch(
        f"/candidate/{candidate_id}",
        json={
            "first_name": "test updated",
            "last_name": "test updated",
        },
        headers={"Authorization": f"Bearer {access_token}"}
        )
    assert response.status_code == 200

def test_delete_candidate():

    response = client.delete(
        f"/candidate/{candidate_id}",
        headers={"Authorization": f"Bearer {access_token}"}
        )

    assert response.status_code == 204

def test_invalid_params():
    response = client.get(
        "/user/62659610-5087-4c59-9fd8-983c69467c97",
        headers={"Authorization": f"Bearer {access_token}"}

        )
    assert response.status_code == 403

def test_get_all_candidates():
    response = client.get(
        "/candidate/",
        headers={"Authorization": f"Bearer {access_token}"}
        )
    assert response.status_code == 200

def test_generate_csv():
    response = client.get(
        "/candidate/generate-report/",
        headers={"Authorization": f"Bearer {access_token}"}
        )
    assert response.status_code == 200
     
def test_user_conflict_and_remove():
    response = client.post("/user", json={
        "first_name": "test",
        "last_name": "test",
        "email": "test@email.com",
        "password": "test"
    })
    assert response.status_code == 409

    response = client.delete(
        f"/user/{user_id}",
        headers={"Authorization": f"Bearer {access_token}"}
        )

    assert response.status_code == 204

def test_invalid_login():
    response = client.post("/login", data={
        "username": "hello",
        "password": "world",
    })
    assert response.status_code == 404