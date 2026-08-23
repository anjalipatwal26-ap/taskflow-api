from pydantic import BaseModel, Field
from typing import Optional, Literal
from datetime import datetime

TaskStatus = Literal["Pending", "In Progress", "Completed"]
TaskPriority = Literal["Low", "Medium", "High"]

class TaskCreate(BaseModel):
    title: str = Field(..., max_length=255)
    description: Optional[str] = None
    status: TaskStatus = "Pending"
    priority: TaskPriority = "Medium"
    due_date: Optional[datetime] = None

class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, max_length=255)
    description: Optional[str] = None
    status: Optional[TaskStatus] = None
    priority: Optional[TaskPriority] = None
    due_date: Optional[datetime] = None

class TaskResponse(BaseModel):
    id: str
    title: str
    description: Optional[str]
    status: str
    priority: str
    due_date: Optional[datetime]
    user_id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
class AIAnalysisResponse(BaseModel):
    task_id: str
    suggested_priority: str
    category: str
    summary: str
    suggestion: str