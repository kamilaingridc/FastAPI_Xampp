from typing import List 
from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.carro_model import CarroModel
from schemas.carro_schema import CarroSchema
from core.deps import get_session

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=CarroSchema)
async def post_carro(carro: CarroSchema, db: AsyncSession = Depends(get_session)):
    
    novo_carro = CarroModel(
        nome=carro.nome, 
        marca=carro.marca, 
        ano=carro.ano
        )
    
    db.add(novo_carro)
    await db.commit()
    
    return novo_carro

@router.get("/", response_model=List[CarroSchema])
async def get_carros(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CarroModel)
        result = await session.execute(query)
        carros: List[CarroModel] = result.scalars().all()
        
        return carros

@router.get("/{carro_id}", response_model=CarroSchema, status_code=status.HTTP_200_OK)
async def get_carros(carro_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CarroModel).filter(CarroModel.id == carro_id)
        result = await session.execute(query)
        carro = result.scalar_one_or_none()
        
        if carro:
            return carro
        else:
            raise HTTPException(detail="Carro not found.", status_code=status.HTTP_404_NOT_FOUND)


@router.put("/{carro_id}", response_model=CarroSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_carro(carro_id: int, carro: CarroSchema, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CarroModel).filter(CarroModel.id == carro_id)
        result = await session.execute(query)
        carro_up = result.scalar_one_or_none()
        
        if carro_up:
             carro_up.nome = carro.nome
             carro_up.marca = carro.marca
             carro_up.ano = carro.ano
             
             await session.commit()
             return carro_up
         
        else:
            raise HTTPException(detail="Carro not found.", status_code=status.HTTP_404_NOT_FOUND)
        
@router.delete("/{carro_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_carro (carro_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CarroModel).filter(CarroModel.id == carro_id)
        result = await session.execute(query)
        carro_del = result.scalar_one_or_none()
        if carro_del:
            await session.delete(carro_del)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail="Car not found.", status_code=status.HTTP_404_NOT_FOUND)
        
        
        