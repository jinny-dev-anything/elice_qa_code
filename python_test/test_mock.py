import requests
import responses

@responses.activate

def test_api_with_mock():
    responses.add(method=responses.GET,
                  url="http://example.com/api",
                  json={"message": "mocked response"},
                  status=200)
    
    response = requests.get("http://example.com/api")

    assert response.json() == {"message": "mocked response"}
    assert len(responses.calls) == 1