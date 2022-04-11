from typing import Type, Union
from enum import Enum
from pydantic import BaseModel


def from_tuple(model: Type['BaseModel'], data: Union[list, tuple]):
    temp = enumerate(model.__fields__.keys())
    return model(**{key: data[i] for i, key in temp})


class AiringStatus(Enum):
        Finihsed = "1111111"
        Burning = "1111110"
        TypesettingFinished = "1111100"
        ProofreadFinished = "1111000"
        PolishTranslated = "1110000"
        EnglishTranslated = '1100000'
        OriginalAvailable = "1000000"
        NotYetAired = "0000000"


class EpisodeModel(BaseModel):
    serie_id: int
    episode_num: int
    status: Union[AiringStatus, str]


class UserModel(BaseModel):
    login: str
    password: str
    email: str