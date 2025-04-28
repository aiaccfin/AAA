from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from pathlib import Path
from fastapi.responses import JSONResponse
import os
router = APIRouter()

BASE_DIR = Path("./tmp")


@router.get("/listfolder/{folder_name}")
def list_specific_folder(folder_name: str):
    cwd = Path(os.getcwd())
    target_folder = cwd / folder_name

    if not target_folder.exists():
        return {"error": f"Folder '{folder_name}' not found in {cwd}"}

    files = []
    for item in target_folder.iterdir():
        files.append({
            "name": item.name,
            "type": "directory" if item.is_dir() else "file",
            "size": item.stat().st_size,
            "last_modified": item.stat().st_mtime
        })

    return {
        "cwd": str(cwd),
        "target_folder": str(target_folder),
        "items": files
    }



@router.get("/list-current")
def list_current_directory():
    cwd = os.getcwd()
    files = os.listdir(cwd)
    return {"cwd": cwd, "files": files}


@router.get("/list-tmp")
def list_jack_directory():
    if not BASE_DIR.exists():
        return JSONResponse(content={"error": "Directory not found."}, status_code=404)

    items = []
    for item in BASE_DIR.iterdir():
        items.append({
            "name": item.name,
            "type": "directory" if item.is_dir() else "file",
            "size": item.stat().st_size,
            "last_modified": item.stat().st_mtime
        })

    return {"items": items}