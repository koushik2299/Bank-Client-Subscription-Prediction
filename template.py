import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')

project_name = 'MLClassifier'

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirments.txt",
    "setup.py",
    "Notebooks",
    "templates/index.html",
    "hello1.txt"
]

for file_path in list_of_files:
    file_path = Path(file_path)
    file_dir,file_name = os.path.split(file_path)

    if file_dir !="":
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f"Creating Directory: {file_dir} and Creating File {file_name}")
    
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
        with open(file_path,"w") as f:
            pass
            logging.info(f"Creating Empty File {file_path}")

    else:
        logging.info(f"{file_path} exists")
