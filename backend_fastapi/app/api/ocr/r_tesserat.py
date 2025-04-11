from fastapi import APIRouter, Depends, File, UploadFile, HTTPException
import os, uuid, pytesseract

from pdf2image import convert_from_path

router = APIRouter()
@router.get("/test")
def root(): return {"OCR": "IMG"}

@router.post("/tesserat")
async def pdf_to_text_tesseract(oUploadFile: UploadFile = File(...)):
    try:
        # Define temp paths
        tmp_dir = "./tmp/pdf_img"
        os.makedirs(tmp_dir, exist_ok=True)

        pdf_path = os.path.join(tmp_dir, f"{uuid.uuid4()}_{oUploadFile.filename}")
        with open(pdf_path, "wb") as f:
            f.write(await oUploadFile.read())

        # Convert PDF pages to images
        images = convert_from_path(pdf_path)

        # Run OCR on each page
        extracted_text = ""
        for i, img in enumerate(images):
            text = pytesseract.image_to_string(img)
            extracted_text += f"\n\n--- Page {i + 1} ---\n{text}"

        # Clean up
        os.remove(pdf_path)

        return {"text": extracted_text.strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))