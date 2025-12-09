from __future__ import annotations

from typing import Any, Dict, List, Optional
from data.payload import ReqInfo
from pydantic import BaseModel, Field


class AmountItem(BaseModel):
    taxHeadCode: str
    amount: float


class Locality(BaseModel):
    code: str


class Address(BaseModel):
    buildingName: Optional[str] = None
    doorNo: Optional[str] = None
    street: Optional[str] = None
    locality: Optional[Locality] = None
    pincode: Optional[str] = None


class Citizen(BaseModel):
    name: Optional[str] = None
    mobileNumber: Optional[str] = None


class Challan(BaseModel):
    citizen: Optional[Citizen]
    businessService: str
    consumerType: Optional[str] = None
    taxPeriodFrom: Optional[int] = None
    taxPeriodTo: Optional[int] = None
    tenantId: str
    address: Optional[Address] = None
    amount: Optional[List[AmountItem]] = Field(default_factory=list)

class ChallanRequest(BaseModel):
    Challan: Challan
    RequestInfo: ReqInfo.RequestInfo


__all__ = ["AmountItem", "Locality", "Address", "Citizen", "Challan", "RequestInfoLocal", "ChallanRequest"]
