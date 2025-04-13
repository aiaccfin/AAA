from pydantic import BaseModel, Field
from typing import List, Optional

class InvoiceItem(BaseModel):
    description: str
    quantity: int
    rate: float
    amount: float

class InvoiceModel(BaseModel):
    vendor:str
    invoice_to: str
    address: str
    invoice_number: str
    date: str
    due_date: str
    terms: str
    service_description: str
    items: List[InvoiceItem]
    message: Optional[str]
    subtotal: float
    discount: float
    tax: float
    total: float
    balance_due: float
