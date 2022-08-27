from fastapi import APIRouter, status, HTTPException, Depends
from ..schemas import Create_Vote
from .. import oauth2
from ..database import get_db
from .. import models
from sqlalchemy.orm import Session

router = APIRouter(
    tags=['Votes']
)

@router.post("/votes", status_code=status.HTTP_201_CREATED)
def create_vote(data: Create_Vote, user_id:int = Depends(oauth2.get_current_user), db: Session = Depends(get_db)):

    if data.dir == 1:
        # check if users already like the code or not
        vote = db.query(models.Vote).filter(models.Vote.code_id == data.code_id, models.Vote.user_id == user_id).first()
        if vote is None:
            # we need to check the code exist or not
            code = db.query(models.Code).filter(models.Code.id == data.code_id).first()
            if code is None:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'There is no code with id {data.code_id}')    
            entry = models.Vote(code_id = data.code_id, user_id = user_id)
            db.add(entry)
            db.commit()
            return {"Message":"Successfully added the vote"}
        else:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f'The user {user_id} already vote for code id {data.code_id}')
    else:
        # this means dislike
        vote = db.query(models.Vote).filter(models.Vote.code_id == data.code_id, models.Vote.user_id == user_id)
        if vote.first() is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The user did not like the code, like first')
        else:
            vote.delete(synchronize_session=False)
            db.commit()
            return {"Message":"Successfully deleted the vote"}