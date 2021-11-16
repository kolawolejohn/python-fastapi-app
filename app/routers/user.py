from typing import  List
from fastapi import  Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas, utils
from .. database import get_db


router = APIRouter(
   prefix='/users',
   tags=['Users']
)

@router.get('/', response_model=List[schemas.User])
async def get_users(db: Session = Depends(get_db)):
   users = db.query(models.User).all()
   return users

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

   ##hash the password

   hashed_password = utils.hash(user.password)
   user.password = hashed_password
   new_user = models.User(**user.dict())
   db.add(new_user)
   db.commit()
   db.refresh(new_user)
   return  new_user


@router.get('/{id}', response_model=schemas.User)
async def get_user(id: int, db: Session = Depends(get_db)):
   user = db.query(models.User).filter(models.User.id == id).first()
   if not user:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'user with id: {id} not found')
   return user


@router.put('/{id}', response_model=schemas.User)
async def update_user(id: int, user: schemas.UserCreate, db: Session = Depends(get_db)):
   
   user_query = db.query(models.User).filter(models.User.id == id)
   updated_user = user_query.first()
   if updated_user == None:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'user with id: {id} not found')
   user_query.update(user.dict(), synchronize_session=False)
   db.commit()
   return user_query.first()


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(id: int, db: Session = Depends(get_db)):
   user = db.query(models.User).filter(models.User.id == id)

   if user.first() == None:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'user with id: {id} not found')
   user.delete(synchronize_session=False)
   db.commit()
   return Response(status_code=status.HTTP_204_NO_CONTENT)