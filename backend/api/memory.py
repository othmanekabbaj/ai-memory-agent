from fastapi import APIRouter

from schemas.conversation_event import ConversationEvent
from schemas.project_memory import ProjectMemory
from services.memory_service import MemoryService

router = APIRouter(prefix="/memory", tags=["Memory"])

service = MemoryService()


@router.post("/event", response_model=ProjectMemory)
def process_event(event: ConversationEvent):
    return service.process_event(event)

@router.get("/context")
def get_context():
    return {
        "context": service.get_context()
    }