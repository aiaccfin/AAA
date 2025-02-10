from fastapi import APIRouter, Depends

from app.utils.u_auth_py import authent
from app.api.v1 import r_ocr

router = APIRouter()

router.include_router(r_ocr.router,  tags=["OCR: OCR"] , dependencies=[Depends(authent)])

# router.include_router(r_ocr_txt.router,  prefix="/ocr_txt", tags=["OCR: Text"] , dependencies=[Depends(authent)])
# router.include_router(r_ocr_img.router,  prefix="/ocr_img", tags=["OCR: Image"], dependencies=[Depends(authent)])

@router.get("/")
def root(): return {"r_ocr": "OCR Setup"}
