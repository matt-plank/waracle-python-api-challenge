from fastapi import APIRouter, Depends, Response

from ..spec import get_spec

router = APIRouter()


@router.get("")
async def get(spec: str = Depends(get_spec)):
    return Response(spec)
