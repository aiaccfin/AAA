from typing import Optional
from datetime import date
from sqlmodel import SQLModel, Field


class InvoiceBase(SQLModel):
    invoice_number: str
    biz_id: int
    biz_name: str
    customer_id: int
    customer_name: str
    client_id: int
    client_name: str
    client_address: str
    client_payment_method: str
    issue_date: date
    due_date: date
    payment_status: str  # could also be Enum
    item_description: str
    item_quantity: float
    item_unit_price: float
    item_tax_rate: float
    item_tax: float
    item_amount: float
    invoice_total_amount: float
    invoice_recurring: bool = False
    invoice_note: Optional[str] = None


class Invoice(InvoiceBase, table=True):
    __tablename__ = "invoices" 
    id: Optional[int] = Field(default=None, primary_key=True)


class InvoiceCreate(InvoiceBase):
    pass


class InvoiceRead(InvoiceBase):
    id: int

class InvoiceUpdate(SQLModel):
    invoice_number: Optional[str] = None
    biz_id: Optional[int] = None
    biz_name: Optional[str] = None
    customer_id: Optional[int] = None
    customer_name: Optional[str] = None
    client_id: Optional[int] = None
    client_name: Optional[str] = None
    client_address: Optional[str] = None
    client_payment_method: Optional[str] = None
    issue_date: Optional[date] = None
    due_date: Optional[date] = None
    payment_status: Optional[str] = None
    item_description: Optional[str] = None
    item_quantity: Optional[float] = None
    item_unit_price: Optional[float] = None
    item_tax_rate: Optional[float] = None
    item_tax: Optional[float] = None
    item_amount: Optional[float] = None
    invoice_total_amount: Optional[float] = None
    invoice_recurring: Optional[bool] = None
    invoice_note: Optional[str] = None