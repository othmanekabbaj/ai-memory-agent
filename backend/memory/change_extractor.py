from llm.ollama_client import OllamaClient
from schemas.conversation_event import ConversationEvent
from schemas.project_changes import ProjectChanges
from schemas.project_memory import ProjectMemory
from utils.prompt_loader import load_prompt


class ChangeExtractor:
    def __init__(self):
        self.client = OllamaClient()

    def extract(
        self,
        current_memory: ProjectMemory,
        event: ConversationEvent,
    ) -> ProjectChanges:

        base_prompt = load_prompt("extract_changes.txt")

        prompt = f"""
{base_prompt}

Current Project Memory:

{current_memory.model_dump_json(indent=2)}

Conversation:

User:
{event.user_message}

Assistant:
{event.assistant_message}
"""

        response = self.client.chat(prompt)

        print("\n===== EXTRACTED CHANGES =====\n")
        print(response)
        print("\n=============================\n")

        return ProjectChanges.model_validate_json(response)