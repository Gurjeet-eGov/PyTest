from pydantic import BaseModel, Field, ValidationError
from typing import List, Optional

class Workflow(BaseModel):
    action: str