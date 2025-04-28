from fastapi import APIRouter, Depends

from app.api.vm.user import r_group, r_role, r_user_new, r_user_login
from app.api.vm.ar import arRouter
from app.api.vm.docman import docRouter
from app.utils.u_auth_py import authent

vmRouter = APIRouter()

# vmRouter.include_router(arRouter)
vmRouter.include_router(docRouter)
vmRouter.include_router(r_user_login.router, prefix="/user",  tags=["xai_user"], dependencies=[Depends(authent)])
vmRouter.include_router(r_user_new.router,   prefix="/user",  tags=["xai_user"], dependencies=[Depends(authent)])
vmRouter.include_router(r_role.router, prefix="/role",  tags=["xai_role"], dependencies=[Depends(authent)])
vmRouter.include_router(r_group.router,prefix="/group", tags=["xai_group"],dependencies=[Depends(authent)])

