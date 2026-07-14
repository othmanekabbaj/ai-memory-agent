from memory.context_generator import ContextGenerator
from memory.memory_engine import MemoryEngine
from memory.memory_store import MemoryStore
from schemas.conversation_event import ConversationEvent
from schemas.project_memory import ProjectMemory


class MemoryService:
    def __init__(self):
        self.engine = MemoryEngine()
        self.store = MemoryStore()
        self.context_generator = ContextGenerator()

    def process_event(
        self,
        event: ConversationEvent,
    ) -> ProjectMemory:

        memory = self.store.load()

        updated_memory = self.engine.update(
            current_memory=memory,
            event=event,
        )

        self.store.save(updated_memory)

        return updated_memory

    def get_context(self) -> str:
        """
        Load the current project memory and generate
        a Markdown context for future AI conversations.
        """

        memory = self.store.load()

        return self.context_generator.generate(memory)