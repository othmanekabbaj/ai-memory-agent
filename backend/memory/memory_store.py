import json
from pathlib import Path

from schemas.project_memory import ProjectMemory


class MemoryStore:

    def __init__(self):
        self.memory_file = (
            Path(__file__)
            .resolve()
            .parent
            .parent
            .parent
            / "storage"
            / "project_memory.json"
        )

    def load(self) -> ProjectMemory:
        if not self.memory_file.exists():
            return ProjectMemory()

        with open(self.memory_file, "r", encoding="utf-8") as file:
            data = json.load(file)

        return ProjectMemory.model_validate(data)

    def save(self, memory: ProjectMemory):
        self.memory_file.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(self.memory_file, "w", encoding="utf-8") as file:
            json.dump(
                memory.model_dump(),
                file,
                indent=2,
                ensure_ascii=False,
            )