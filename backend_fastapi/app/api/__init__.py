from fastapi import APIRouter, Depends

from app.api.v1 import r_root, system_setup, biz_setup, r_ocr
from app.api.vm import vmRouter
from app.utils.u_auth_py import authent

apiRouter = APIRouter()

apiRouter.include_router(vmRouter)
apiRouter.include_router(r_root.router,                                tags=["Root"],           dependencies=[Depends(authent)])
apiRouter.include_router(system_setup.router,  prefix="/system_setup", tags=["System Setup"],   dependencies=[Depends(authent)])
apiRouter.include_router(biz_setup.router,     prefix="/biz_setup",    tags=["BizEntity Setup"],dependencies=[Depends(authent)])
apiRouter.include_router(r_ocr.router,         prefix="/ocr",          tags=["OCR"],            dependencies=[Depends(authent)])
