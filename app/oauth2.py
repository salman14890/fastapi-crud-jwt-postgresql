import os
from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

SECRET_KEY = os.getenv('codeblog_secret_key')
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRY_MINUTES = 30

def create_access_token(data: dict):
    to_encode = data.copy()
    expiry_of_token = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRY_MINUTES)
    #expiry = json.dumps(expiry_of_token, default=defaultconverter)
    to_encode.update({"exp":expiry_of_token})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token":encoded_jwt, "token_type":"bearer"}

def defaultconverter(o):
  if isinstance(o, datetime):
      return o.__str__()

def verify_payload(token):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    username: int = payload.get("user_id")
    
    if username is None:
        return None
    return username

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        username = verify_payload(token)
        if username is None:
            return None
        return username
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f'Signature has been expired')
        

