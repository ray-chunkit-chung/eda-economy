from pydantic import BaseModel


class News(BaseModel):
    title: str
    content: str
    url: list[str]
