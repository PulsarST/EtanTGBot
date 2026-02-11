from datetime import datetime
from typing import List

from pydantic import BaseModel, Field


class StudentsReview(BaseModel):
    """Student Review is a schema for students reviews in DB."""

    causes: List[str]
    """causes(List[str]): a list of causes why student sends good, bad review about professor, or activity in university."""

    mark: int
    """mark(int): defeined in [1, 10] and describes a studenet opinion in int about professor, or activity in univeristy."""

    professors_name: str
    """professors_name(str): name of professor."""

    date: datetime = Field(default_factory=datetime.now)
    """date(datetime): the date when review was sended."""

    subject: str
    """subject(str): a name of subject."""


class ProfessorSchema(BaseModel):
    """The schema for describing a professors in DB"""

    name: str
    """name(str): the name of professr"""


class SubjectSchema(BaseModel):
    """The schema for describing a subjects in DB"""

    name: str
    """name(str): the name of subject"""
