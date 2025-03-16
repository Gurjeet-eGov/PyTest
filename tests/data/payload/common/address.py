from pydantic import BaseModel, Field, ValidationError
from typing import List, Optional, Dict, Any

class Locality(BaseModel):
    code: str
    name: str


class Address(BaseModel):
    landmark: str
    city: str
    district: str
    region: str
    pincode: str
    locality: Locality
    geoLocation: Dict[str, Any]