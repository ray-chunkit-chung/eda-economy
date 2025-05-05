import json

from openai import OpenAI

from typing import Type, TypeVar, Dict, Any
from pydantic import BaseModel
from models.test import News

__all__ = [
    "get_web_search_response",
]


T = TypeVar("T", bound=BaseModel)


def get_web_search_response(
    api_key: str,
    model: str,
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
    client = OpenAI(api_key=api_key)

    response = client.responses.parse(
        model=model,
        temperature=0,
        tools=[{"type": "web_search_preview"}],
        text_format=response_model,
        input=input_text,
    )

    result = response.output_parsed
    result = json.loads(result.model_dump_json())
    return result
