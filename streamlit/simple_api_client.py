import logging
import httpx

LIST_TEAMS_ENDPOINT = "/v0/teams/"

logger = logging.getLogger(__name__) 

def call_api_endpoint(
    base_url: str,
    api_endpoint: str, 
    api_params: dict = None
) -> httpx.Response:

    try:
        with httpx.Client(base_url=base_url) as client: 
            logger.debug(f"base_url: {base_url}, api_endpoint: {api_endpoint}, api_params: {api_params}")
            response = client.get(api_endpoint, params=api_params)
            response.raise_for_status()
            logger.debug(f"Response JSON: {response.json()}")
            return response
    except Exception as e:
        logger.error(f"Unexpected error occurred: {str(e)}")
        return httpx.Response(status_code=500, content=b"Unexpected error")