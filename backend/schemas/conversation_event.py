from pydantic import BaseModel, Field


class ConversationEvent(BaseModel):
    chat_id: str
    timestamp: str

    user_message: str
    assistant_message: str

    changed_files: list[str] = Field(default_factory=list)
    git_diff: str = ""