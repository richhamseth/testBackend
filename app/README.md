# GitHub API Service

A simple HTTP web server API that fetches a GitHub user's gists using GitHub API.

---

## Features
- `GET /<username>` → returns a JSON list of the user’s public gists.
- Includes gist ID, description, files list and count , URL, creation date and updatio date.

---

## Requirements
- Docker (for containerized setup)

---

## Run and test app using Docker
- To Test App using Docker
```bash
git clone https://github.com/EqualExperts-Assignments/equal-experts-analytical-decisive-ample-power-d68cba5014e0.git
cd app
docker build -t api-server:test --target test .
docker run --rm api-server:test
```

- To Run using Docker
```bash
git clone https://github.com/EqualExperts-Assignments/equal-experts-analytical-decisive-ample-power-d68cba5014e0.git
cd app
docker build -t api-server:run --target run .
docker run -p 8080:8080 api-server:run

# To Run Container in demon
docker run -d -p 8080:8080 api-server:run
```

- To Test App Manually Various way can be followed as mentioned below:
  - Use Browser(Chrome/Safari) use this url --> http://0.0.0.0:8080/<USERNAME> (eg: http://0.0.0.0:8080/octocat)
  - Use Curl Request to Check via linux machine ``` curl -v http://0.0.0.0:8080/<USERNAME> ```
  - Postman can used to check the API

---

## Local Run and test (without Docker)

- Requirements
  - Python 3.9+

```bash
pip install flask requests

# To Test app
pip install pytest requests-mock
cd app
pytest -v functional_test.py

# To Run app
cd app
python app.py
```