from memory.memory_engine import MemoryEngine
from memory.memory_store import MemoryStore
from schemas.conversation_event import ConversationEvent

store = MemoryStore()

# Load existing memory
memory = store.load()

# First run only
if not memory.project_name:
    memory.project_name = "AI Memory Agent"
    memory.summary = "An AI assistant that remembers software projects."
    memory.current_task = "Build the memory engine"

event = ConversationEvent(
    user_message="Implement the Ollama client.",
    assistant_message="Created the OllamaClient class to communicate with Qwen."
)

engine = MemoryEngine()

updated_memory = engine.update(
    current_memory=memory,
    event=event,
)

store.save(updated_memory)

print(updated_memory)