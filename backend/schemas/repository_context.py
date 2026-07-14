from pydantic import BaseModel, Field


class FileContext(BaseModel):
    path: str
    extension: str = ""
    size: int = 0
    lines: int = 0

    analysis: dict = Field(
        default_factory=dict
    )


class RepositoryContext(BaseModel):
    files: list[str] = Field(
        default_factory=list
    )

    file_contexts: list[FileContext] = Field(
        default_factory=list
    )