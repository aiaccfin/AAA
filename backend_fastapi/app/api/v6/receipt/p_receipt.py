from fastapi import APIRouter, Depends, File, UploadFile, HTTPException, UploadFile, Form 

from sqlmodel import Session, select

from app.db.pg.crud  import c_receipt
from app.db.pg.model  import m_receipt
from app.db.pg.p_conn import get_session
from app.services import s_inv, s_file_system
from app.utils import u_is_textpdf 


router = APIRouter()

@router.get("/")
def get_all(db: Session = Depends(get_session),):
    return c_receipt.get_all( db)


@router.get("/{one_id}")
def get_one(one_id: int, db: Session = Depends(get_session)):
    return c_receipt.get_one(one_id=one_id, db=db)

@router.post("/new")
def post_new_receipt(receipt: m_receipt.receiptCreate, db: Session = Depends(get_session)):
    return c_receipt.create_receipt(receipt=receipt, db=db)

@router.patch("/{one_id}")
def update_1_receipt(one_id: int, receipt: m_receipt.receiptUpdate, db: Session = Depends(get_session)):
    return c_receipt.update_receipt(one_id=one_id, receipt=receipt, db=db)


@router.delete("/{one_id}")
def delete_1_receipt(one_id: int, db: Session = Depends(get_session)):
    return c_receipt.delete_receipt(one_id=one_id, db=db)


@router.post("/upload", tags=["receipt"], summary="Upload receipt PDF")
async def ocr(oUploadFile: UploadFile = File(...), db: Session = Depends(get_session)):
    print(f"Received file: {oUploadFile.filename}")
    try:
        pdf_name, pdf_folder = await s_file_system.save_pdf(oUploadFile)

        if u_is_textpdf.is_textpdf(oUploadFile):
            _type = "text-pdf"
            inv_json = s_inv.inv_textpdf(oUploadFile, pdf_name, pdf_folder)
        else:
            _type = "img-pdf"
            inv_json = s_inv.inv_imgpdf(pdf_name, pdf_folder)

        print("DEBUG inv_json:", inv_json)
        
        # receipt_data = m_receipt.receiptCreate.model_validate(inv_json["content"])
        receipt_data = m_receipt.receiptCreate.model_validate(inv_json)

        saved_receipt = c_receipt.create_receipt(receipt_data, db)
        
        return {"type": _type , "content": inv_json}
    
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")


