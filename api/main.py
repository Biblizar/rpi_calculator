from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from calculator import RPNCalculator
from database import Database
from fastapi.responses import StreamingResponse
import csv
import io
db = Database()

app = FastAPI()

calculator = RPNCalculator()
class CalculationRequest(BaseModel):
    expression: str

class CalculationResponse(BaseModel):
    result: float

@app.post('/calculate',response_model=CalculationResponse)
async def calculate(request: CalculationRequest):
    try:
        result = calculator.calculate(request.expression)
        await db.insert_operation(expression=request.expression, result=result)
    except Exception as exception:
        raise HTTPException(status=400, detail=str(exception))

@app.get('/export_csv', response_class=StreamingResponse)
async def export_csv():
    operations = await db.get_all_operations()

    csv_file = io.StringIO()
    writer = csv.writer(csv_file)

    writer.writerow(["Expression", "Result"])

    for operation in operations:
        writer.writerow([operation["expression"], operation["result"]])
    
    csv_file.seek(0)

    return StreamingResponse(
        iter([csv_file.getvalue()]),
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=operations.csv"}
    )