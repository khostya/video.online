from fastapi import Depends
from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv

from app.user.user import User, current_active_user

account_router = InferringRouter()


@cbv(account_router)
class AccountRouter:

    @account_router.get("/authenticated-route")
    async def authenticated_route(self, user: User = Depends(current_active_user)):
        return {"message": f"Hello {user.email}!"}
