# Python API Test Automation Framework

A Python-based API test automation framework built with **Pytest** and **Requests**.

The project focuses on building a maintainable API test automation structure with reusable API clients, authentication handling, fixtures, parametrized tests, mocking, configuration management, and CI/CD integration.

GitHub Actions runs the mock test suite to avoid external API dependency and rate limiting in CI.

## Features

- API testing with Python and Requests
- Reusable HTTP client with `requests.Session`
- Authentication flow testing
- CRUD API testing
- Pytest fixtures
- Parametrized test cases
- Mock-based API testing with `unittest.mock`
- Timeout and error handling
- Environment-based configuration
- GitHub Actions CI/CD

## Project Structure

```text
python-api-framework/
│
├── api/
│   ├── client.py
│   └── auth.py
│
├── test_data/
│   └── auth_data.py
│
├── tests/
│   ├── conftest.py
│   ├── test_auth.py
│   ├── test_auth_mock.py
│   ├── test_first_api.py
│   └── test_first_api_mock.py
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── config.py
├── requirements.txt
├── .gitignore
└── README.md
Architecture

The framework separates generic HTTP communication from API-specific operations.

Tests
  │
  ├── auth.login()
  └── auth.me()
        │
        ↓
    client.py
        │
        ├── get()
        ├── post()
        ├── put()
        └── delete()
        │
        ↓
   send_request()
        │
        ↓
 requests.Session
        │
        ↓
   API Endpoint

client.py handles generic HTTP communication, while auth.py contains authentication-related API operations.

Testing Strategy

The project includes both real API tests and mock-based tests.

Authentication
Successful login
Invalid credentials
Current authenticated user
Invalid endpoint
Timeout handling
CRUD
GET
POST
PUT
DELETE
Mock Testing

External HTTP requests can be replaced with mocked responses using unittest.mock.

Mock tests cover:

Login
Current user
GET
POST
PUT
DELETE

This allows API behavior to be tested without depending on the external API during mock test execution.

Pytest Fixtures

Reusable test setup is implemented with Pytest fixtures.

The authenticated fixture performs the login operation and prepares the session with the required authorization header for tests that require an authenticated user.

Parametrized Testing

Pytest parametrization is used when the same test logic needs to be executed with different inputs.

For example:

@pytest.mark.parametrize(
    "endpoint, expected_status",
    [
        ("/auth/does-not-exist", 404),
        ("/http/500", 500),
    ]
)
def test_endpoint_error(endpoint, expected_status):
    response = get(endpoint)

    assert response.status_code == expected_status
Configuration

Framework configuration is managed through config.py.

Environment variables can be used to override:

BASE_URL
TIMEOUT

Authentication test data is maintained separately in test_data/auth_data.py.

The following environment variables can be used for authentication:

API_USERNAME
API_PASSWORD
Installation

Clone the repository and install the dependencies:

git clone https://github.com/eugurkarakaya/python-api-framework.git

cd python-api-framework

pip install -r requirements.txt
Running Tests

Run all tests:

python -m pytest -v

Run authentication tests:

python -m pytest tests/test_auth.py -v

Run mock tests:

python -m pytest tests/test_auth_mock.py tests/test_first_api_mock.py -v
CI/CD

GitHub Actions is used to automatically run the mock API test suite when changes are pushed to the repository.

The workflow:

Checks out the repository
Sets up Python
Installs dependencies
Runs the mock test suite
Reports the test result
Technologies
Python
Pytest
Requests
unittest.mock
Git
GitHub Actions
Purpose

This project was built to practice and demonstrate API test automation using Python, with a focus on maintainable test structure, reusable API communication, test isolation, mocking, parametrization, configuration management, and continuous integration.