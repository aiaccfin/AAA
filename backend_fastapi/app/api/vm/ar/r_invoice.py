from fastapi import APIRouter,HTTPException

from app.models.m_user import Role
from app.schemas.s_invoice import InvoiceModel
from app.schemas.s_email_reminder import EmailReminderRequest
from app.db.x_mg_conn import invoice_collection
from app.utils.u_load_invoice import load_invoice_from_file
from app.utils.gmail.senders.invoice_sender import send_invoice_reminder

router = APIRouter()

@router.post("/load", response_model=Role)
async def import_invoice(invoice: InvoiceModel):
    try:
        raw_invoice_data = load_invoice_from_file()
        invoice = InvoiceModel(**raw_invoice_data)
                
        result = await invoice_collection.insert_one(invoice.dict())
        return {
            "status":      "success",
            "inserted_id": str(result.inserted_id)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/list")
async def get_invoices():
    try:
        invoices_cursor = invoice_collection.find()
        invoices = []
        async for invoice in invoices_cursor:
            invoice["_id"] = str(invoice["_id"])  # Convert ObjectId to str
            invoices.append(invoice)
        return invoices
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/email-reminder")
def send_invoice_email(data: EmailReminderRequest):
    try:
        send_invoice_reminder(
            vendor=data.vendor,
            invoice_number=data.invoice_number,
            due_date=data.due_date,
            balance_due=data.balance_due,
        )
        return {"message": "Reminder email sent"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    

@router.post("/email-received")
def send_email_received(data: EmailReminderRequest):
    try:
        send_invoice_reminder(
            vendor=data.vendor,
            invoice_number=data.invoice_number,
            due_date=data.due_date,
            balance_due=data.balance_due,
        )
        return {"message": "Thank you email sent"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))