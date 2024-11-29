from fastapi import FastAPI, HTTPException
from pymongo import MongoClient

app = FastAPI()

client = MongoClient("mongodb://localhost:27017/")
db = client["mqtt_db"]
collection = db["messages"]

@app.get("/status_count/")
def status_count(start_time: float, end_time: float):
    try:
        pipeline = [
            {"$match": {"timestamp": {"$gte": start_time, "$lte": end_time}}},
            {"$group": {"_id": "$status", "count": {"$sum": 1}}}
        ]
        results = list(collection.aggregate(pipeline))
        return {item["_id"]: item["count"] for item in results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
