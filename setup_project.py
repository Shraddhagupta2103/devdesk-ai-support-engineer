from pathlib import Path


folders = [
    "data/github_docs",
    "data/internal_docs",

    "src",
    "src/nlp",
    "src/rag",
    "src/llm",

    "scripts",

    "app",

    "models",

    "tests",
]


for folder in folders:
    Path(folder).mkdir(
        parents=True,
        exist_ok=True
    )


print("Project structure created successfully!")