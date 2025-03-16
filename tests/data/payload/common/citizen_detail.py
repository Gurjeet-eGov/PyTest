from pydantic import BaseModel, Field, ValidationError
from typing import List, Optional, Dict, Any

class Role(BaseModel):
    id: Any
    name: str
    code: str
    tenantId: str


class Citizen(BaseModel):
    name: str
    type: str
    mobileNumber: str
    roles: List[Role]
    tenantId: str