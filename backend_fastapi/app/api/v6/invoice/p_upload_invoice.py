from fastapi import APIRouter, Depends, File, UploadFile, HTTPException, UploadFile, Form 

import os

from base64 import b64encode

from app.services import s_ocr, s_gocr, s_file_system
from app.utils import pdf264

router = APIRouter()

UPLOAD_ROOT = "tmp"

@router.post("/")
async def ocr(oUploadFile: UploadFile = File(...)):
    try:
        pdf_name, pdf_folder = await s_file_system.save_pdf(oUploadFile)

        if s_ocr.is_text_pdf(oUploadFile):
            _type = "text-pdf"
            ocr_text = s_ocr.pdf_reader(oUploadFile, pdf_name, pdf_folder)
        else:
            _type = "img-pdf"
            ocr_text = s_ocr.img_pdf(pdf_name, pdf_folder)
    
        
        return {"type": _type , "content": ocr_text}
    
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")


@router.post("/save2pg")
async def save2db():
    s_ocr.save2db()


