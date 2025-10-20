import pytest
import requests
from app import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

# Positive test cases
# Test fetching gists for a valid GitHub user
def test_get_user_gists_positive(client):
    response = client.get("/octocat")
    assert response.status_code == 200, "Expected status 200"

    data = response.get_json()
    assert isinstance(data, list), "Response should be in list"

    if len(data) > 0:
        gist = data[0]
        for key in ["id", "url", "files", "created_at", "updated_at", "description", "total_files"]:
            assert key in gist, f"Missing key: {key}"

# Negative test cases
# Test fetching gists for a non-existing GitHub user
def test_get_nonexisting_user_gists_negative(client):
    response = client.get("/octocatsample")
    assert response.status_code == 404, "Expected status 404 for non-existent user"

    data = response.get_json()
    assert "error" in data, "Response should contain an error message"
    assert data["error"] == "User not found or GitHub API error", "Unexpected error message"
    assert data["status"] == "error", "Status should be error"
    assert data["status_code"] == 404, "Status code should be 404"
    assert "message" in data, "Response should contain a message"

# Test handling of GitHub API timeout
def test_github_timeout_negative(client, requests_mock):
    requests_mock.get("https://api.github.com/users/octocat/gists", exc=requests.exceptions.Timeout)

    response = client.get("/octocat")
    assert response.status_code == 500
    assert response.get_json()["error"] == "Internal server error"