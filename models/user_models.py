from pydantic import BaseModel

# Definición de modelos de estado
class UserIn(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    username: str
    balance: int
