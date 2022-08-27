from fastapi import status, APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, oauth2
from ..database import get_db
from ..schemas import Create_Post, Update_Post, Token

router = APIRouter(tags = ['Codes'])

@router.get("/codes")
def get_all_codes(user_id:int = Depends(oauth2.get_current_user),db : Session = Depends(get_db)):
    
    #username = user_id
    #if username is None:
    #    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")
    codes  = db.query(models.Code).filter(models.Code.user_id == user_id).all()
    return codes

@router.get("/codes/{id}")
def get_one_code(id :int, user_id:int = Depends(oauth2.get_current_user)  ,db : Session = Depends(get_db)):
    #username =14
    #if username is None:
    #    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")
    code = db.query(models.Code).filter(models.Code.id == id).first()
    return code

@router.post("/codes", status_code=status.HTTP_201_CREATED)
def create_post(data: Create_Post, user_id:int =Depends(oauth2.get_current_user),  db:Session = Depends(get_db)):
    entry = models.Code(user_id = user_id, **data.dict())
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry

@router.put("/codes/{id}")
def update_post(id: int, data: Update_Post,user_id:int =Depends(oauth2.get_current_user), db: Session = Depends(get_db)):
    code = db.query(models.Code).filter(models.Code.id == id)

    if code.first() is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f'The code with id {id} not found on the server')
    code.update(data.dict())
    db.commit()
    db.refresh(code.first())
    return code.first()

@router.delete("/codes/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int,user_id:int =Depends(oauth2.get_current_user), db: Session = Depends(get_db)):
    code = db.query(models.Code).filter(models.Code.id == id)

    if code.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The code with id {id} not found on the server')
    code.delete()
    db.commit()
    return {"Message":"The code has been deleted successfully from the server"}