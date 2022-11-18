from . import db

sistersdb = db.sisters

async def add_sister(s1_id: int, s2_id: int):
    x = await sistersdb.find_one({"s1_id": s1_id})
    if x:
        list = x["sisters"]
        if not s2_id in list:
            list.append(s2_id)
            return await sistersdb.update_one({"s1_id": s1_id}, {"$set": {"sisters": list}}, upsert=True)
    
