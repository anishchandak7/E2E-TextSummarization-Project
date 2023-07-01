import setuptools

# Get ReadMe file description.
with open("README.md", "r", encoding='utf-8') as file:
    long_description = file.read()

__VERSION__ = "0.0.0"
AUTHOR_NAME = "anishchandak7"
REPO_NAME = "E2E-TextSummarization-Project"
SRC_PROJECT_NAME = "textSummarizer"
AUTHOR_EMAIL = "chandakanish7@gmail.com"


setuptools.setup(

    name=SRC_PROJECT_NAME,
    version=__VERSION__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="NLP-project python package",
    long_description=long_description,
    long_description_content = "text/markdown",
    url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker" : f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)