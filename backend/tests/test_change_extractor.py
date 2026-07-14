from memory.change_extractor import ChangeExtractor
from schemas.conversation_event import ConversationEvent

event = ConversationEvent(
    user_message="Implement a MemoryStore to save the project memory.",
    assistant_message="""
Created a MemoryStore class.
It can load and save ProjectMemory to a JSON file.
"""
)

extractor = ChangeExtractor()

changes = extractor.extract(event)

print(changes)