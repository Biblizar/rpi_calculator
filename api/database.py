import os
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId

class Database:
    def __init__(self):
        self.client = AsyncIOMotorClient(os.getenv("MONGODB_URI", "mongodb://mongo:27017"))
        self.db = self.client["rpn_calculator_db"]
        self.operations = self.db["operations"]
    
    async def insert_operation(self, expression: str, result: float):
        await self.operations.insert_one({
            "expression": expression,
            "result": result
        })

    async def get_all_operations(self):
        cursor = self.operations.find({})
        return await cursor.to_list(length=1000)