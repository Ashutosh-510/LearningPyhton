from typing import Annotated
from pydantic import BaseModel, Field

class User(BaseModel):
    name: Annotated[str, Field(
        min_length=3,
          max_length=50
    )]
    age: Annotated[int, Field(gt=0)]