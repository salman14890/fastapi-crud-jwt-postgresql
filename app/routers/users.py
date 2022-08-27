from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models
from ..schemas import Create_User, Create_User_Response
from .. import utils

router = APIRouter(tags=['Users'])

@router.post("/users", status_code=status.HTTP_201_CREATED, response_model=Create_User_Response)
def create_user(data: Create_User, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == data.email).first()
    if user is None:
        hashed_password = utils.hash_password(data.password)
        data.password = hashed_password
        entry = models.User(**data.dict())
        db.add(entry)
        db.commit()
        db.refresh(entry)
        return entry
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f'The user with email {data.email} already exist')
