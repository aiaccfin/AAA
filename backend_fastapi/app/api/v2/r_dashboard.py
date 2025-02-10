from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_dashboard():
    return {
        "message": "Welcome to the Dashboard",
        "notifications": {
            "bank_statement": "No new messages",
            "receipt_bill_logs": "No new messages",
            "invoice_summary": "No new messages"
        }
    }
