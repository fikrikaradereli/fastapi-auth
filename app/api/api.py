from fastapi import APIRouter

from . import root, auth, users

router = APIRouter()

router.include_router(root.router)
router.include_router(auth.router)
router.include_router(users.router)