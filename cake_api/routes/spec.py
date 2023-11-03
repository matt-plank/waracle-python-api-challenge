from fastapi import APIRouter, Depends

from ..spec import get_spec

router = APIRouter()


@router.get("")
async def get(spec: dict = Depends(get_spec)):
    return spec
