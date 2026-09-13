import requests
from pathlib import Path


OUTPUT_DIR = Path("data/github_docs")

OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True
)


DOCUMENTS = {
    "about_rest_api.md":
        "/en/rest/about-the-rest-api/about-the-rest-api",

    "getting_started.md":
        "/en/rest/using-the-rest-api/getting-started-with-the-rest-api",

    "authentication.md":
        "/en/rest/authentication/authenticating-to-the-rest-api",

    "troubleshooting.md":
        "/en/rest/using-the-rest-api/troubleshooting-the-rest-api",

    "rate_limits.md":
        "/en/rest/using-the-rest-api/rate-limits-for-the-rest-api",

    "best_practices.md":
        "/en/rest/using-the-rest-api/best-practices-for-using-the-rest-api",

    "repositories.md":
        "/en/rest/repos/repos",

    "repository_contents.md":
        "/en/rest/repos/contents",

    "quickstart.md":
        "/en/rest/quickstart",

    "authentication_overview.md":
        "/en/rest/authentication",
}


BASE_URL = "https://docs.github.com/api/article"


for filename, pathname in DOCUMENTS.items():

    print(f"Downloading {filename}...")

    response = requests.get(
        BASE_URL,
        params={"pathname": pathname},
        timeout=30
    )

    response.raise_for_status()

    data = response.json()

    content = data["body"]

    file_path = OUTPUT_DIR / filename

    file_path.write_text(
        content,
        encoding="utf-8"
    )

    print(f"Saved: {file_path}")


print("\nAll GitHub documentation downloaded successfully!")