from pydantic import BaseModel, Field


class Website(BaseModel):
    """
    A Pydantic model representing a URL.

    Attributes:
        url (str): The URL string.
    """

    name: str = Field(..., description="The website name.")
    url: str = Field(..., description="The URL string.")


class Websites(BaseModel):
    """
    A Pydantic model representing a website.

    """

    topic: str = Field(..., description="The topic of the websites.")
    websites: list[Website] = Field(
        ...,
        description="A list of URLs where the topic information can be found.",
    )
