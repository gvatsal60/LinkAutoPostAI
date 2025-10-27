'''
Configuration module for loading environment variables securely.
'''
import os


def load_env():
    """Load environment variables from a .env file securely."""
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError as e:
        raise ImportError(
            "Missing 'python-dotenv'. Install it with 'pip install python-dotenv'."
        ) from e


def get_env_variable(key):
    """Retrieve an environment variable securely."""
    # Load .env file
    load_env()

    os.environ[key] = os.getenv(key)
    if not os.environ[key]:
        raise EnvironmentError(f"Missing required environment variable: {key}")
    return os.environ[key]
