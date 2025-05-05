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
    llm_model: str,
    input_text: str = "What was a positive news story from today?",
    response_model: Type[T] = News,
) -> Dict[str, Any]:
    """
    Get a web search response using the OpenAI API.

    Args:
        api_key (str): The OpenAI API key for authentication
        llm_model (str): The name/identifier of the language model to use
        input_text (str, optional): The query text to search for.
            Defaults to "What was a positive news story from today?"
        response_model (Type[BaseModel], optional): The Pydantic model class
            used for parsing the response. Defaults to News.

    Returns:
        Dict[str, Any]: A dictionary containing the parsed response data
            structured according to the response_model schema

    Raises:
        ValueError: If the API key is invalid
        TypeError: If the response_model is not a valid Pydantic model
    """
    client = OpenAI(api_key=api_key)

    response = client.responses.parse(
        model=llm_model,
        temperature=0,
        tools=[{"type": "web_search_preview"}],
        text_format=response_model,
        input=input_text,
    )

    result = response.output_parsed
    result = json.loads(result.model_dump_json())
    return result
