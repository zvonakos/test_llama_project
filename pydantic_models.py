"""Decided to add pydantic to provide validation of data coming to through the requests"""
from pydantic import BaseModel


class Document(BaseModel):
    filename: str
    content: str


class Question(BaseModel):
    question: str
