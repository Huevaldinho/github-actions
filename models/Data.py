from pydantic import BaseModel
from typing import List, Dict, Any, Union

class MockResponseBody(BaseModel):
    """Base class for mock response bodies - can be extended for specific response types"""
    pass

class MockResponse(BaseModel):
    status: int
    headers: Dict[str, str]
    body: Union[Dict[str, Any], List[Dict[str, Any]]]  # Can be either dict or list

class Mock(BaseModel):
    id: str
    name: str
    description: str
    method: str
    path: str
    response: MockResponse

class Data(BaseModel):
    mocks: List[Mock]