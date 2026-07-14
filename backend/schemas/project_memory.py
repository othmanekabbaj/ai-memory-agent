from pydantic import BaseModel, Field


class ProjectMemory(BaseModel):
    """
    Represents the long-term project memory.

    This is the context injected into AI conversations.
    """

    project_name: str = ""

    summary: str = ""

    current_task: str = ""


    # Development history

    completed: list[str] = Field(
        default_factory=list
    )

    todos: list[str] = Field(
        default_factory=list
    )

    decisions: list[str] = Field(
        default_factory=list
    )

    known_issues: list[str] = Field(
        default_factory=list
    )


    # Technical knowledge

    architecture: list[str] = Field(
        default_factory=list
    )

    technical_context: list[str] = Field(
        default_factory=list
    )


    # Repository understanding

    repository_files: list[str] = Field(
        default_factory=list
    )


    repository_summary: list[str] = Field(
        default_factory=list
    )


    repository_architecture: list[str] = Field(
        default_factory=list
    )