from fastapi import APIRouter, Depends

from sqlmodel import Session, select

from app.db.pg.crud  import c_invoice
from app.db.pg.model  import m_invoice
from app.db.pg.p_conn import get_session

router = APIRouter()

@router.get("/test")
def root(): return {"Invoice": "System Setup"}

@router.get("/")
def get_all(db: Session = Depends(get_session),):
    return c_invoice.get_all( db)


@router.get("/{one_id}")
def get_one(one_id: int, db: Session = Depends(get_session)):
    return c_invoice.get_one(one_id=one_id, db=db)


@router.post("/new")
def post_new_invoice(Invoice: m_invoice.InvoiceCreate, db: Session = Depends(get_session)):
    return c_invoice.create_invoice(Invoice=Invoice, db=db)

@router.patch("/{one_id}")
def update_1_invoice(one_id: int, Invoice: m_invoice.InvoiceUpdate, db: Session = Depends(get_session)):
    return c_invoice.update_invoice(one_id=one_id, Invoice=Invoice, db=db)


@router.delete("/{one_id}")
def delete_1_invoice(one_id: int, db: Session = Depends(get_session)):
    return c_invoice.delete_invoice(one_id=one_id, db=db)
