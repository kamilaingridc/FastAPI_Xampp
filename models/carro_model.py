from core.configs import Settings
from sqlalchemy import Column, Integer, String 

# DBBaseModel é a classe declarativa do SQl Alchemy 

class CarroModel(Settings.DBBaseModel):
    __tablename__ = 'carros'
    
    id: int = Column(Integer(), primary_key=True, autoincrement=True)
    nome: str = Column(String(50))
    marca: str = Column(String(50))
    ano: str = Column(String(4))
    