from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from calculator import RPNCalculator
from database import Database
db = Database()

app = FastAPI()

calculator = RPNCalculator()
class CalculationRequest(BaseModel):
    expression: str

class CalculationResponse(BaseModel):
    result: float

@app.get('/')
def root():
    return {"message": "Hello World"}

@app.post('/calculate',response_model=CalculationResponse)
async def calculate(request: CalculationRequest):
    try:
        result = calculator.calculate(request.expression)
        await db.insert_operation(expression=request.expression, result=result)
    except Exception as exception:
        raise HTTPException(status=400, detail=str(exception))
    