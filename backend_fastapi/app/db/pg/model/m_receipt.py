from typing import Optional
from datetime import date
from sqlmodel import SQLModel, Field

class ReceiptBase(SQLModel):
    date: Optional[date] = None # type: ignore
    vendor: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    non: Optional[str] = None
    subtotal: Optional[float] = None  # numeric(10,2) → float
    tax: Optional[float] = None
    total: Optional[float] = None
    payment: Optional[str] = None
    paymentTerm: Optional[str] = None
    reference: Optional[str] = None
    biz_id: Optional[int] = None
    biz_status: Optional[str] = None
    biz_vendor_name: Optional[str] = None
    biz_coa: Optional[str] = None

class Receipt(ReceiptBase, table=True):
    __tablename__ = "receipts"
    id: Optional[int] = Field(default=None, primary_key=True)

class ReceiptCreate(ReceiptBase):
    pass

class ReceiptRead(ReceiptBase):
    id: int

class ReceiptUpdate(SQLModel):
    pass
