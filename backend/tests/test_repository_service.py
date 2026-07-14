import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from services.repository_service import RepositoryService


service = RepositoryService()


context = service.scan_repository(
    "C:/Projets/ai-memory-agent"
)


print(
    f"Files indexed: {len(context.files)}"
)

for file in context.files[:20]:
    print(file)