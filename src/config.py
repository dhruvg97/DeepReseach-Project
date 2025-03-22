# src/config.py
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_openai_key():
    """Get the OpenAI API key from environment variables."""
    api_key = os.getenv("OPENAI_KEY")
    if not api_key:
        raise ValueError("OPENAI_KEY environment variable not set")
    return api_key

def get_tavily_key():
    """Get the OpenAI API key from environment variables."""
    api_key = os.getenv("TAVILY_API_KEY")
    if not api_key:
        raise ValueError("TAVILY_API_KEY environment variable not set")
    return api_key

# Add other configuration functions as needed
def get_config():
    """Get all configuration as a dictionary."""
    return {
        "openai_api_key": get_openai_key(),
        "tavily_api_key":get_tavily_key(),
        # Add other config items here
    }