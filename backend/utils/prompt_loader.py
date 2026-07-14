from pathlib import Path


PROMPTS_DIR = Path(__file__).parent.parent / "prompts"


def load_prompt(filename: str) -> str:
    prompt_path = PROMPTS_DIR / filename

    with open(prompt_path, "r", encoding="utf-8") as file:
        return file.read()