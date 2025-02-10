from fastapi import APIRouter, Depends

from app.utils.u_auth_py import authent
from app.api.v1.system_setup import r_system_setup_coa, r_system_setup_naics

router = APIRouter()

router.include_router(r_system_setup_coa.router,    prefix="/coa",  tags=["System Setup: COA"], dependencies=[Depends(authent)])
router.include_router(r_system_setup_naics.router,  prefix="/naics",tags=["System Setup: NAICS"], dependencies=[Depends(authent)])

@router.get("/")
def root(): return {"SS": "System Setup"}
