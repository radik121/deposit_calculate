from fastapi import APIRouter, status
from schemas.deposit import DepositModels
from .operations import get_calculate_deposit



router = APIRouter(
    prefix="/api/v1",
)


@router.post(
    "/calculation",
    tags=["calculation"],
    status_code=status.HTTP_200_OK,
    summary="Вычисление депозита",
    )
async def calculation_deposit(data: DepositModels) -> dict[str, float]:
    return await get_calculate_deposit(data)