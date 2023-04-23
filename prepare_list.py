from typing import List
from pydantic import Field, BaseModel, validator
from uuid import uuid4, UUID


class Fighter(BaseModel):
    id_: UUID = uuid4()
    name:str = Field(str, min_length=2, max_length=30)
    surname:str = Field(str, min_length=2, max_length=30)
    weight_class:str
    record : List[int]
    position_in_ranking : int = 0

    @validator('name')
    def name_must_be_alpha(cls, v):
        if not v.isalpha():
            raise ValueError("Name must be alpha")
        else:
            return v
    
    @validator('surname')
    def surname_must_be_alpha(cls, v):
        if not v.isalpha():
            raise ValueError("Surname must be alpha")
        else:
            return v
        
    @validator('record')
    def record_length_must_be_two(cls, v):
        if len(v) != 2:
            raise ValueError("Record length must be two")
        elif len(v) == 2 and v[0] < 0 or v[1] < 0:
            raise ValueError("Both record number must be 0 or higher")
        else:
            return v
    
    @validator("weight_class")
    def weight_class_light_middle_or_heavy(cls, v):
        if not v in ["Light", "Middle", "Heavy"]:
            raise ValueError("Weight class must be Light, Middle or Heavy")
        else:
            return v