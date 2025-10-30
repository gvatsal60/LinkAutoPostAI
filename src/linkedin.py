"""
Module to interact with LinkedIn API for posting content.
"""

import requests

REQUEST_TIMEOUT = 10  # seconds

def get_linkedin_author_urn(access_token: str) -> str:
    """
    Retrieve the LinkedIn author's URN using the access token.
    Args:
        access_token (str): LinkedIn API access token.
    Returns:
        str: The URN of the authenticated user.
    Raises:
        KeyError: If the 'sub' key is not present in the response.
        requests.HTTPError: For HTTP errors.
    """

    url = 'https://api.linkedin.com/v2/userinfo'

    headers = {
        'Authorization': f"Bearer {access_token}",
        'X-Restli-Protocol-Version': '2.0.0',
    }

    resp = requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT)
    resp.raise_for_status()  # Raises an HTTPError for bad status codes

    data = resp.json()
    urn_key = 'sub'

    if urn_key not in data:
        raise KeyError(
            f"LinkedIn API response does not contain 'sub' key. Response: {data}"
        )

    urn = data[urn_key]

    _author_urn = f"urn:li:person:{urn}"

    return _author_urn


def linkedin_post_content(access_token: str, message: str):
    """
    Post generated content to LinkedIn.
    Args:
        access_token (str): LinkedIn API access token.
        message (str): The content of the LinkedIn post.
    """

    url = 'https://api.linkedin.com/v2/ugcPosts'

    headers = {
        'Authorization': f"Bearer {access_token}",
        'X-Restli-Protocol-Version': '2.0.0',
        'Content-Type': 'application/json',
    }

    author_urn = get_linkedin_author_urn(access_token=access_token)

    payload = {
        'author': author_urn,
        'lifecycleState': 'PUBLISHED',
        'specificContent': {
            'com.linkedin.ugc.ShareContent': {
                'shareCommentary': {
                    'text': message
                },
                'shareMediaCategory': 'NONE'
            }
        },
        'visibility': {'com.linkedin.ugc.MemberNetworkVisibility': 'PUBLIC'}
    }

    resp = requests.post(url, headers=headers,
                         json=payload, timeout=REQUEST_TIMEOUT)
    resp.raise_for_status()  # Raises an HTTPError for bad status codes
