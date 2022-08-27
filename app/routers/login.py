from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models, utils, oauth2
from fastapi.security import OAuth2PasswordRequestForm
from ..schemas import Token

router = APIRouter(tags=['Logins'])

@router.post("/login")
def user_login(data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == data.username).first()

    if user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'Invalid credentials')
    verify_user = utils.verify_password(data.password, user.password)

    if verify_user:
        token = oauth2.create_access_token(data={"user_id":user.id})
        return token
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'Invalid credentials')

