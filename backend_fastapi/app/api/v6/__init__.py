from fastapi import APIRouter, Depends

from app.api.v6.naics import p_naics
from app.api.v6.invoice import p_invoice, p_upload_invoice
from app.utils.u_auth_py import authent

v6Router = APIRouter()

v6Router.include_router(p_naics.router, prefix="/p_naics", tags=["v6_naics"], dependencies=[Depends(authent)])
v6Router.include_router(p_invoice.router, prefix="/p_invoice", tags=["v6_invoice"], dependencies=[Depends(authent)])
v6Router.include_router(p_upload_invoice.router, prefix="/p_upload_invoice", tags=["v6_upload_invoice"], dependencies=[Depends(authent)])
