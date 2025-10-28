'''
Configuration module for loading environment variables securely.
'''
import os
from pathlib import Path


def load_env():
    """Load environment variables from a .env file securely."""

    env_path = Path(".env")

    if env_path.exists():
        try:
            from dotenv import load_dotenv
            load_dotenv(dotenv_path=env_path,
                        override=True)
        except ImportError as e:
            raise ImportError(
                "Missing 'python-dotenv'. \
                Install it with 'pip install python-dotenv'."
            ) from e


def get_env_variable(key):
    """Retrieve an environment variable securely."""
    # Load .env file
    load_env()

    value = os.getenv(key)

    if value is None:
        raise EnvironmentError(f"Missing required environment variable: {key}")
    return value
