from fastapi import APIRouter, Depends

from app.api.vm.ar import r_invoice
from app.utils.u_auth_py import authent

arRouter = APIRouter()

arRouter.include_router(r_invoice.router, prefix="/invoice",  tags=["xai_ar"], dependencies=[Depends(authent)])
