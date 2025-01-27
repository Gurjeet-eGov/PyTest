from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel

from tests.data.payload import ReqInfo

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


class Service(BaseModel):
    tenantId: str
    serviceCode: str
    description: str
    additionalDetail: Dict[str, Any]
    source: str
    address: Address
    citizen: Citizen


class Workflow(BaseModel):
    action: str


class Model(BaseModel):
    service: Service
    workflow: Workflow
    RequestInfo: ReqInfo.RequestInfo
