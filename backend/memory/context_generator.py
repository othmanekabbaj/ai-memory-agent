from schemas.project_memory import ProjectMemory



class ContextGenerator:


    def generate(
        self,
        memory: ProjectMemory
    ) -> str:



        has_content = any([

            memory.project_name,

            memory.summary,

            memory.current_task,

            memory.completed,

            memory.todos,

            memory.decisions,

            memory.known_issues,

            memory.architecture,

            memory.technical_context,

            memory.repository_summary,

            memory.repository_architecture

        ])



        if not has_content:

            return ""



        lines = []



        lines.append(
            "# AI Memory Context"
        )

        lines.append("")



        #
        # Project
        #

        lines.append(
            "## Project"
        )


        lines.append(
            memory.project_name
            or
            "Unnamed Project"
        )


        lines.append("")



        #
        # Summary
        #

        if memory.summary:


            lines.append(
                "## Summary"
            )


            lines.append(
                memory.summary
            )


            lines.append("")



        #
        # Technical Context
        #

        if memory.technical_context:


            lines.append(
                "## Technical Context"
            )


            for item in memory.technical_context:

                lines.append(
                    f"- {item}"
                )


            lines.append("")



        #
        # Repository Architecture
        #

        if memory.repository_architecture:


            lines.append(
                "## Repository Architecture"
            )


            for item in memory.repository_architecture:

                lines.append(
                    f"- {item}"
                )


            lines.append("")



        #
        # Repository Understanding
        #

        if memory.repository_summary:


            lines.append(
                "## Repository Understanding"
            )


            for item in memory.repository_summary[:50]:

                lines.append(
                    f"- {item}"
                )


            lines.append("")



        #
        # Current task
        #

        if memory.current_task:


            lines.append(
                "## Current Task"
            )


            lines.append(
                memory.current_task
            )


            lines.append("")



        #
        # History
        #

        sections = [

            (
                "Completed",
                memory.completed
            ),

            (
                "TODO",
                memory.todos
            ),

            (
                "Decisions",
                memory.decisions
            ),

            (
                "Known Issues",
                memory.known_issues
            ),

        ]



        for title, items in sections:


            if items:


                lines.append(
                    f"## {title}"
                )


                for item in items:

                    lines.append(
                        f"- {item}"
                    )


                lines.append("")



        lines.append("---")

        lines.append("")


        lines.append(
            "Continue this software project using the context above.\n"
            "Assume completed work has already been implemented.\n"
            "Do not repeat finished tasks.\n"
            "Prioritize the current task."
        )



        return "\n".join(lines)