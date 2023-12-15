from fastapi import Depends,HTTPException,status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from . import schema,database,crud_user
from jose import jwt,JWTError
from typing import Annotated
get_db=database.get_db

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 180

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


# def get_current_user(data:str=Depends(oauth2_scheme)):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     return token.verify_token(data,credentials_exception)
async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> schema.User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    #breakpoint()
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: str = payload.get("id")
        if id is None:
            raise credentials_exception
            
    except JWTError:
        print("ABC")
        raise credentials_exception
    user = crud_user.get_by_id(id, db)

    if user is None:
        raise credentials_exception
    return user





