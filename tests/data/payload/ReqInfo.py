from pydantic import BaseModel, Field

class RequestInfo(BaseModel):
    apiId: str = "Rainmaker"
    authToken: str
    msgId: str = "1737885351657|en_IN"
    userInfo: dict