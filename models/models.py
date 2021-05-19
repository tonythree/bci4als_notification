from typing import List, Optional, ClassVar
from pydantic import BaseModel, validator

class Notification(BaseModel):
    uid: str
    project_id: str
    type: str
    message: str