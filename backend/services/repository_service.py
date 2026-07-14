from memory.repository_store import RepositoryStore
from utils.repository_scanner import RepositoryScanner
from memory.memory_store import MemoryStore


class RepositoryService:


    def __init__(self):

        self.scanner = RepositoryScanner()

        self.repository_store = RepositoryStore()

        self.memory_store = MemoryStore()



    def scan_repository(
        self,
        path: str
    ):


        # Scan repository
        repository_context = self.scanner.scan(
            path
        )


        # Save complete repository analysis

        self.repository_store.save(
            repository_context
        )



        memory = self.memory_store.load()



        #
        # Store file list
        #

        memory.repository_files = (
            repository_context.files
        )



        #
        # Generate repository summary
        #

        memory.repository_summary = (
            self.generate_repository_summary(
                repository_context
            )
        )



        #
        # Detect architecture
        #

        memory.repository_architecture = (
            self.detect_architecture(
                repository_context
            )
        )



        self.memory_store.save(
            memory
        )


        return repository_context



    def generate_repository_summary(
        self,
        repository_context
    ):

        summary = []


        for file in repository_context.file_contexts:


            analysis = file.analysis


            if not analysis:
                continue



            classes = analysis.get(
                "classes",
                []
            )


            functions = analysis.get(
                "functions",
                []
            )



            if classes:

                summary.append(
                    f"{file.path} contains classes: "
                    f"{', '.join(classes)}"
                )



            if functions:

                summary.append(
                    f"{file.path} contains functions: "
                    f"{', '.join(functions)}"
                )



        return summary



    def detect_architecture(
        self,
        repository_context
    ):


        architecture = []

        files = repository_context.files



        if any(
            "api" in file
            for file in files
        ):

            architecture.append(
                "API layer handles HTTP endpoints"
            )



        if any(
            "services" in file
            for file in files
        ):

            architecture.append(
                "Service layer contains business logic"
            )



        if any(
            "schemas" in file
            for file in files
        ):

            architecture.append(
                "Schema layer defines data models"
            )



        if any(
            "memory" in file
            for file in files
        ):

            architecture.append(
                "Memory layer manages AI memory operations"
            )



        if any(
            "llm" in file
            for file in files
        ):

            architecture.append(
                "LLM layer manages AI model communication"
            )



        if any(
            "utils" in file
            for file in files
        ):

            architecture.append(
                "Utility layer contains reusable tools"
            )


        return architecture