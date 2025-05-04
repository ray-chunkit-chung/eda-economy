import os
import json

from dotenv import load_dotenv
from openai import OpenAI

from typing import Type, TypeVar, Dict, Any, Optional
from pydantic import BaseModel
from models import News

__all__ = [
    "get_web_search_response",
]

# Load environment variables from .env file
load_dotenv(dotenv_path=".env")
OPENAI_API_KEY: Optional[str] = os.getenv("OPENAI_API_KEY")
MODEL_WEB_SEARCH: str = os.getenv("MODEL_WEB_SEARCH", "gpt-4o-mini")
# WEB_SEARCH_MODEL = os.getenv("WEB_SEARCH_MODEL", "gpt-4.1-mini")

client = OpenAI(api_key=OPENAI_API_KEY)

T = TypeVar("T", bound=BaseModel)


def get_web_search_response(
    input_text: str = "What was a positive news story from today?",
    response_model: Type[T] = News,
) -> Dict[str, Any]:
    """
    Get a web search response using the OpenAI API.

    Args:
        input_text: The query text to search for
        response_model: The Pydantic model to use for parsing the response

    Returns:
        A dictionary with the parsed response data
    """
    response = client.responses.parse(
        model=MODEL_WEB_SEARCH,
        temperature=0,
        tools=[{"type": "web_search_preview"}],
        text_format=response_model,
        input=input_text,
    )

    result = response.output_parsed
    result = json.loads(result.model_dump_json())
    return result
