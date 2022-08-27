from fastapi import FastAPI, status, Depends, HTTPException
from . import models
from .database import Engine
from .routers import codes, users, login, votes

app = FastAPI()

#create all tables if not exists
models.Base.metadata.create_all(bind=Engine)

app.include_router(codes.router)
app.include_router(users.router)
app.include_router(login.router)
app.include_router(votes.router)