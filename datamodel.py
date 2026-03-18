from pydantic import BaseModel
from typing import List

class InputData(BaseModel):
    name: str
    gender: str
    birthyear: int
    birthplace: str
    residence: str

    question1: int
    question2: int
    question3: int
    question4: int
    question5: int
    question6: int
    question7: int
    question8: int
    question9: int
    question10: int
    question11: int
    question12: int
    question13: int
    question14: int
    question15: int
    question16: int
    question17: int
    question18: int
    question19: int
    question20: int

    job: str
    pets: List[str]
    message: str