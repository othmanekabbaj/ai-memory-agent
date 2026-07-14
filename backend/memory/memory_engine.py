from memory.change_extractor import ChangeExtractor
from memory.memory_merger import MemoryMerger
from schemas.project_memory import ProjectMemory
from schemas.conversation_event import ConversationEvent


class MemoryEngine:
    def __init__(self):
        self.extractor = ChangeExtractor()
        self.merger = MemoryMerger()

    def update(
        self,
        current_memory: ProjectMemory,
        event: ConversationEvent,
    ) -> ProjectMemory:

        changes = self.extractor.extract(
            current_memory=current_memory,
            event=event,
        )

        if not changes.is_project_update:
            return current_memory

        updated_memory = self.merger.merge(
            current_memory,
            changes,
        )

        return updated_memory