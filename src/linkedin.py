'''
Module to interact with LinkedIn API for posting content.
'''
import requests


def linkedin_post_content(access_token: str, author_urn: str, message: str) -> requests.Response:
    """
    Post generated content to LinkedIn.
    Args:
        access_token (str): LinkedIn API access token.
        author_urn (str): The URN of the author (e.g., "urn:li:person:xxxx").
        message (str): The content of the LinkedIn post.
    """

    req_timeout = 10  # seconds

    url = 'https://api.linkedin.com/v2/ugcPosts'

    headers = {
        'Authorization': f"Bearer {access_token}",
        'X-Restli-Protocol-Version': '2.0.0',
        'Content-Type': 'application/json'
    }

    payload = {
        'author': author_urn if author_urn.startswith('urn:li:person:') else f"urn:li:person:{author_urn}",
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
                         json=payload, timeout=req_timeout)
    resp.raise_for_status()  # Raises an HTTPError for bad status codes

    return resp
