'''
Generate LinkedIn post content using LangChain and OpenAI.
'''
from http import HTTPStatus
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.messages import SystemMessage, HumanMessage
import requests

from config import get_env_variable


def post_content(access_token: str, author_urn: str, message: str) -> None:
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

    resp = requests.post(
        url,
        headers=headers,
        json=payload,
        timeout=req_timeout
    )

    if resp.status_code != HTTPStatus.CREATED:
        print('Error posting content to LinkedIn:', resp.status_code, resp.text)
        exit(1)


def generate_linkedin_post(model_name: str, api_key: str) -> str:
    """
    Generate a LinkedIn post about software engineering best practices.
    Args:
        model_name (str): The name of the language model to use.
        api_key (str): The API key for authentication.
    Returns:
        str: Generated LinkedIn post content.
    """
    # 1️⃣ System message: defines the role and style
    system_msg = SystemMessage("""
    You are a professional LinkedIn content creator for software engineers and tech leaders. Write one engaging, insightful, and concise LinkedIn post (5-7 sentences maximum) that offers an actionable tip or a key insight specifically about software engineering best practices, system design, or modern development methodologies (like DevOps or microservices). The tone should be professional yet approachable, and you must include at least three relevant emojis and a set of appropriate hashtags. Do not make it sound like a sales pitch or advertisement.
    """)

    # 2️⃣ Human message: defines the specific task
    human_msg = HumanMessage("""
    Generate a single, informational LinkedIn post focusing on a software engineering best practice. Keep it professional, short (5-7 sentences), and engaging. Include relevant emojis and hashtags.
    """)

    messages = [
        system_msg,
        human_msg
    ]

    model = ChatGoogleGenerativeAI(
        model=model_name,
        api_key=api_key,
    )

    response = model.invoke(messages)
    return response.content


if __name__ == '__main__':
    # Set your API key
    try:
        API_KEY = get_env_variable('MODEL_API_KEY')
        MODEL_NAME = get_env_variable('MODEL_NAME')
        ACCESS_TOKEN = get_env_variable('LINKEDIN_ACCESS_TOKEN')
        AUTHOR_URN = get_env_variable('LINKEDIN_AUTHOR_URN')
    except (ImportError, EnvironmentError) as e:
        print(e)
        exit(1)

    post_content_txt = generate_linkedin_post(MODEL_NAME, API_KEY)
    # post_content(ACCESS_TOKEN, AUTHOR_URN, post_content_txt)

    print('Generated LinkedIn Post Content:\n', post_content_txt)  # FIXME
