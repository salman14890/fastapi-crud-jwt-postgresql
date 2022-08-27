from passlib.context import CryptContext

password_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def hash_password(password: str):
    hashed_password = password_context.hash(password)
    return hashed_password

def verify_password(password:str, hashed_password:str):
    result = password_context.verify(password,hashed_password)
    return result