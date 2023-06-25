import os
from pathlib import Path
import logging
from typing import List

# Setup logging configuration and format.
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


def setupProjectTemplate(files:List):

    for file in files:
        windowsPathObj = Path(file)
        file_dir, file_name = os.path.split(windowsPathObj)
        
        if file_dir != "":
            os.makedirs(file_dir, exist_ok=True)
            logging.info(f"Creating directory: {file_dir} for the file {file_name}")
        
        if not os.path.exists(windowsPathObj) or os.path.getsize(windowsPathObj) == 0:
            with open(windowsPathObj, 'w') as f:
                pass
            logging.info(f"Created an empty file: {file_name} at {file_dir}")
        else:
            logging.info(f"{file_name} at {file_dir} already exists!")


def main():
    """Template Main function."""

    project_name = "textSummarizer"

    logging.info(f"Initiating project setup...")
    files_list = [
    ".github/workflows/.gitkeep", #CI/CD deployment
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/configuration.py",
    "config/config.yaml",
    "params.yaml",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/"
    ]

    setupProjectTemplate(files_list)
    logging.info(f"Project template successfully created.")

main()
