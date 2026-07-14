from schemas.project_changes import ProjectChanges
from schemas.project_memory import ProjectMemory


class MemoryMerger:

    def merge(
        self,
        memory: ProjectMemory,
        changes: ProjectChanges,
    ) -> ProjectMemory:

        if changes.project_name and not memory.project_name:
            memory.project_name = changes.project_name

        if changes.summary and not memory.summary:
            memory.summary = changes.summary

        if changes.current_task:
            memory.current_task = changes.current_task

        self._append_unique(memory.completed, changes.completed)
        self._append_unique(memory.todos, changes.todos)
        self._append_unique(memory.decisions, changes.decisions)
        self._append_unique(memory.known_issues, changes.known_issues)
        self._append_unique(memory.architecture, changes.architecture)
        self._append_unique(memory.technical_context, changes.technical_context)

        if memory.current_task in memory.completed:
            memory.current_task = ""

        return memory

    @staticmethod
    def _append_unique(target: list[str], source: list[str]):
        for item in source:
            if item and item not in target:
                target.append(item)