import os

from schemas.repository_context import (
    RepositoryContext,
    FileContext,
)

from utils.code_analyzer import CodeAnalyzer


class RepositoryScanner:

    IGNORE_DIRS = {
        ".git",
        ".idea",
        ".vscode",
        "node_modules",
        "__pycache__",
        "venv",
        ".venv",
        "env",
        ".env",
        "dist",
        "build",
        "site-packages",
        "target",
        ".pytest_cache"
    }

    IGNORE_FILES = {
        ".pyc",
        ".log"
    }


    def __init__(self):
        self.analyzer = CodeAnalyzer()


    def scan(self, path: str) -> RepositoryContext:

        files = []
        file_contexts = []


        for root, dirs, filenames in os.walk(path):

            dirs[:] = [
                d for d in dirs
                if d not in self.IGNORE_DIRS
            ]


            for file in filenames:

                if any(
                    file.endswith(ext)
                    for ext in self.IGNORE_FILES
                ):
                    continue


                full_path = os.path.join(
                    root,
                    file
                )

                relative_path = os.path.relpath(
                    full_path,
                    path
                )


                files.append(relative_path)


                file_contexts.append(
                    self.analyze_file(
                        full_path,
                        relative_path
                    )
                )


        return RepositoryContext(
            files=sorted(files),
            file_contexts=file_contexts
        )


    def analyze_file(
        self,
        full_path: str,
        relative_path: str
    ) -> FileContext:

        try:

            with open(
                full_path,
                "r",
                encoding="utf-8"
            ) as f:

                lines = len(
                    f.readlines()
                )


        except Exception:

            lines = 0


        _, extension = os.path.splitext(
            relative_path
        )


        size = os.path.getsize(
            full_path
        )


        analysis = self.analyzer.analyze(
            full_path
        )


        return FileContext(
            path=relative_path,
            extension=extension,
            size=size,
            lines=lines,
            analysis=analysis
        )