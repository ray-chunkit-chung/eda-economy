from pydantic import BaseModel, Field


class News(BaseModel):
    title: str
    content: str
