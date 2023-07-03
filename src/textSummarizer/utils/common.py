import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger # Custom logging
from ensure import ensure_annotations # To ensure params types are correctly passed while calling a function
from box import ConfigBox # To access Key:value pair data using Key name as well instead of passing it as a string.
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:

    """
    Reads the YAML file and returns its contents as an instance of `ConfigBox`.

    Args:
        path_to_yaml (str): Path Object
    
    Raises:
        ValueError: if yaml file is empty
        e: empty file
    
    Return:
        ConfigBox type content 
    """
    try :
        with open(path_to_yaml) as yaml_file:
            data = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully.")
            return ConfigBox(data)
    except BoxValueError:
        raise ValueError("YAML File is Empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_dirs: list, verbose = True):

    """
    Creates directories

    Args:
        path_to_dirs (list): list of directories
        verbose (boolean): If True, function will log creation of directories.
    """

    for path in path_to_dirs:
        os.makedirs(path, exist_ok=True)
        if verbose == True:
            logger.info(f"Created directory at: {path}")
    
@ensure_annotations
def get_size(path: Path) -> str:
    
    """
    Returns size of a given filepath in KB

    Args:
        path (Path): path of the file.
    
    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"