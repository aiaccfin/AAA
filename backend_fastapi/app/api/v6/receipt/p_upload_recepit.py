from fastapi import APIRouter, Depends, File, UploadFile, HTTPException, UploadFile, Form 
from app.services import s_inv, s_file_system
from app.utils import u_is_textpdf 
from sqlmodel import Session
from app.db.pg.model import m_invoice
from app.db.pg.p_conn import get_session
from app.db.pg.crud import c_invoice

router = APIRouter()

@router.post("/")
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
        
        # invoice_data = m_invoice.InvoiceCreate.model_validate(inv_json["content"])
        invoice_data = m_invoice.InvoiceCreate.model_validate(inv_json)

        saved_invoice = c_invoice.create_invoice(invoice_data, db)
        
        return {"type": _type , "content": inv_json}
    
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")


