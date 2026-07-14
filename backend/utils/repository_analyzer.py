from schemas.repository_context import RepositoryContext



class RepositoryAnalyzer:


    def analyze(
        self,
        repository: RepositoryContext
    ) -> list[str]:


        architecture = []


        folders = set()



        for file in repository.files:

            parts = file.split("\\")


            if len(parts) > 1:

                folders.add(
                    parts[1]
                )



        for folder in sorted(folders):


            if folder == "api":

                architecture.append(
                    "API layer handles HTTP endpoints"
                )


            elif folder == "services":

                architecture.append(
                    "Service layer contains business logic"
                )


            elif folder == "memory":

                architecture.append(
                    "Memory layer manages AI memory operations"
                )


            elif folder == "utils":

                architecture.append(
                    "Utility layer contains reusable tools"
                )


            elif folder == "schemas":

                architecture.append(
                    "Schema layer defines data models"
                )


            elif folder == "llm":

                architecture.append(
                    "LLM layer manages AI model communication"
                )


        return architecture