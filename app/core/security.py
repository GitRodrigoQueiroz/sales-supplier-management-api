from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def autenticar_usuario(token: str = Depends(oauth2_scheme)):
    if token != "meu_token_secreto":
        raise HTTPException(status_code=401, detail="Token inválido")
    return {"user": "Rodrigo"}