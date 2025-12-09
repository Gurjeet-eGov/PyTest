from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field
from data.payload import ReqInfo


# Document model
class Document(BaseModel):
    documentType: str
    fileStoreId: str
    i18nKey: Optional[str] = None
    status: Optional[str] = None


# Process Instance model
class ProcessInstance(BaseModel):
    id: Optional[str] = None
    tenantId: Optional[str] = None
    businessService: Optional[str] = None
    businessId: Optional[str] = None
    action: Optional[str] = None
    moduleName: Optional[str] = None
    state: Optional[str] = None
    comment: Optional[str] = None
    documents: Optional[Any] = None
    assignes: Optional[Any] = None


# Audit Details model
class AuditDetails(BaseModel):
    createdBy: Optional[str] = None
    lastModifiedBy: Optional[str] = None
    createdTime: Optional[int] = None
    lastModifiedTime: Optional[int] = None


# Locality model
class Locality(BaseModel):
    code: str
    name: Optional[str] = None
    label: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    area: Optional[str] = None
    children: Optional[List[Any]] = Field(default_factory=list)
    materializedPath: Optional[str] = None


# Geo Location model
class GeoLocation(BaseModel):
    latitude: Optional[float] = None
    longitude: Optional[float] = None


# Address model
class Address(BaseModel):
    tenantId: Optional[str] = None
    doorNo: Optional[str] = None
    plotNo: Optional[str] = None
    id: Optional[str] = None
    landmark: Optional[str] = None
    city: Optional[str] = None
    district: Optional[str] = None
    region: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    pincode: Optional[str] = None
    buildingName: Optional[str] = None
    street: Optional[str] = None
    locality: Optional[Locality] = None
    geoLocation: Optional[GeoLocation] = None
    additionalDetails: Optional[Dict[str, Any]] = None


# Role model
class Role(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    code: Optional[str] = None
    tenantId: Optional[str] = None


# User/Owner model
class User(BaseModel):
    id: Optional[str] = None
    uuid: Optional[str] = None
    userName: Optional[str] = None
    password: Optional[str] = None
    salutation: Optional[str] = None
    name: Optional[str] = None
    gender: Optional[str] = None
    mobileNumber: Optional[str] = None
    emailId: Optional[str] = None
    altContactNumber: Optional[str] = None
    pan: Optional[str] = None
    aadhaarNumber: Optional[str] = None
    permanentAddress: Optional[str] = None
    permanentCity: Optional[str] = None
    permanentPinCode: Optional[str] = None
    correspondenceCity: Optional[str] = None
    correspondencePinCode: Optional[str] = None
    correspondenceAddress: Optional[str] = None
    active: Optional[bool] = None
    dob: Optional[int] = None
    pwdExpiryDate: Optional[int] = None
    locale: Optional[str] = None
    type: Optional[str] = None
    signature: Optional[str] = None
    accountLocked: Optional[bool] = None
    roles: Optional[List[Role]] = Field(default_factory=list)
    fatherOrHusbandName: Optional[str] = None
    bloodGroup: Optional[str] = None
    identificationMark: Optional[str] = None
    photo: Optional[str] = None
    createdBy: Optional[str] = None
    createdDate: Optional[int] = None
    lastModifiedBy: Optional[str] = None
    lastModifiedDate: Optional[int] = None
    tenantId: Optional[str] = None
    alternatemobilenumber: Optional[str] = None
    ownerInfoUuid: Optional[str] = None
    isPrimaryOwner: Optional[bool] = None
    ownerShipPercentage: Optional[float] = None
    ownerType: Optional[str] = None
    institutionId: Optional[str] = None
    status: Optional[str] = None
    documents: Optional[Any] = None
    relationship: Optional[str] = None


# Property model
class Property(BaseModel):
    id: Optional[str] = None
    propertyId: Optional[str] = None
    surveyId: Optional[str] = None
    linkedProperties: Optional[Any] = None
    tenantId: Optional[str] = None
    accountId: Optional[str] = None
    oldPropertyId: Optional[str] = None
    status: Optional[str] = None
    address: Optional[Address] = None
    acknowldgementNumber: Optional[str] = None
    propertyType: Optional[str] = None
    ownershipCategory: Optional[str] = None
    owners: Optional[List[User]] = Field(default_factory=list)
    institution: Optional[Any] = None
    creationReason: Optional[str] = None
    usageCategory: Optional[str] = None
    noOfFloors: Optional[int] = None
    landArea: Optional[float] = None
    superBuiltUpArea: Optional[float] = None
    source: Optional[str] = None
    channel: Optional[str] = None
    documents: Optional[Any] = None
    units: Optional[List[Any]] = Field(default_factory=list)
    additionalDetails: Optional[Dict[str, Any]] = None
    auditDetails: Optional[AuditDetails] = None
    workflow: Optional[Any] = None
    AlternateUpdated: Optional[bool] = None
    processInstance: Optional[Any] = None


# Main SewerageConnection Update model
class SwUpdate(BaseModel):
    id: Optional[str] = None
    tenantId: str
    propertyId: str
    applicationNo: Optional[str] = None
    applicationStatus: Optional[str] = None
    status: Optional[str] = None
    connectionNo: Optional[str] = None
    oldConnectionNo: Optional[str] = None
    documents: Optional[List[Document]] = Field(default_factory=list)
    plumberInfo: Optional[Any] = None
    roadType: Optional[str] = None
    roadCuttingArea: Optional[float] = None
    roadCuttingInfo: Optional[Any] = None
    connectionExecutionDate: Optional[int] = None
    connectionCategory: Optional[str] = None
    connectionType: Optional[str] = None
    additionalDetails: Optional[Dict[str, Any]] = None
    processInstance: Optional[ProcessInstance] = None
    auditDetails: Optional[AuditDetails] = None
    connectionHolders: Optional[Any] = None
    applicationType: Optional[str] = None
    dateEffectiveFrom: Optional[int] = None
    oldApplication: Optional[bool] = None
    channel: Optional[str] = None
    disconnectionExecutionDate: Optional[int] = None
    proposedWaterClosets: Optional[int] = None
    proposedToilets: Optional[int] = None
    noOfWaterClosets: Optional[int] = None
    noOfToilets: Optional[int] = None
    isDisconnectionTemporary: Optional[bool] = None
    disconnectionReason: Optional[str] = None
    property: Optional[Property] = None


# Main model for SewerageConnection request
class Model(BaseModel):
    SewerageConnection: SwUpdate
    RequestInfo: ReqInfo.RequestInfo
