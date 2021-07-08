from fastapi import APIRouter

router = APIRouter(
    prefix="",
    tags=[],
)

@router.get("/health_check")
def health_check():
    return "success"