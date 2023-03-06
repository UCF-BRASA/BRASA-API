

from fastapi import APIRouter, HTTPException

from models.prediction import TestResponse, TestRequest


router = APIRouter(prefix='/users', tags=['Users'])

@router.post(
    "/add",
    response_model=TestResponse,
    name="This name shows:in the auto-generated SwaggerHubs docs",
)
async def add(data_input: TestRequest):
    try:
        name = data_input.name
        other = data_input.other

        return TestResponse(salve=f'name={name} -> other={other}')
    
    except Exception:
        raise HTTPException(status_code=404, detail="Some Exception")
