from pydantic import BaseModel, Field


class ProjectChanges(BaseModel):
    is_project_update: bool = False

    project_name: str = ""
    summary: str = ""
    current_task: str = ""

    completed: list[str] = Field(default_factory=list)
    todos: list[str] = Field(default_factory=list)
    decisions: list[str] = Field(default_factory=list)
    known_issues: list[str] = Field(default_factory=list)
    architecture: list[str] = Field(default_factory=list)
    technical_context: list[str] = Field(default_factory=list)