from fastapi import APIRouter, Depends

from app.api.v6.naics import p_naics
from app.utils.u_auth_py import authent

v6Router = APIRouter()

v6Router.include_router(p_naics.router, prefix="/p_naics", tags=["v6_naics"], dependencies=[Depends(authent)])
