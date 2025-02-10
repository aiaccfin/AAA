from fastapi import APIRouter, Depends, File, UploadFile, HTTPException
import dotenv

from base64 import b64encode

from app.services import s_ocr, s_gocr, s_file_system
from app.utils import pdf264

router = APIRouter()

CFG = dotenv.dotenv_values(".env")
ENDPOINT_URL = CFG['GOOGLE_VISION_ENDPOINT']
API_KEY = CFG['GOOGLE_CLOUD_API_KEY']
IMG_LOC = "rawbs_Page_5.jpg"

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


@router.post("/save2db")
async def save2db():
    s_ocr.save2db()


@router.post("/save2mongo")
async def save2db():
    s_ocr.save2db()


@router.post("/Google_OCR_Image_Only")
def google_ocr():
    result = s_gocr.request_ocr(ENDPOINT_URL, API_KEY, IMG_LOC)
    ocr_result = result.json()['responses'][0]['textAnnotations']
    return ocr_result


