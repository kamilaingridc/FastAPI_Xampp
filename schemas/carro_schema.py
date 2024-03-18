from typing import Optional 
from pydantic import BaseModel as SCBaseModel

class CarroSchema(SCBaseModel):
    id: Optional[int] = None
    nome: str
    marca: str
    ano: str
    
    class Config:
        orm_mode = True
        