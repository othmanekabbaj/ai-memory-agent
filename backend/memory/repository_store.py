import json
from pathlib import Path

from schemas.repository_context import RepositoryContext


class RepositoryStore:

    def __init__(self):
        self.path = Path("storage/repository_context.json")

    def load(self) -> RepositoryContext:

        if not self.path.exists():
            return RepositoryContext()

        with open(self.path, "r", encoding="utf-8") as file:
            data = json.load(file)

        return RepositoryContext(**data)


    def save(self, context: RepositoryContext):

        self.path.parent.mkdir(
            exist_ok=True
        )

        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(
                context.model_dump(),
                file,
                indent=2
            )