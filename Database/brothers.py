from . import db

brothersdb = db.brothers

async def add_brother(b1_id: int, b2_id: int):
    x = await brothersdb.find_one({"b1_id": b1_id})
    if x:
        list = x["brothers"]
        if not b2_id in list:
            list.append(b2_id)
            return await brothersdb.update_one({"b1_id": b1_id}, {"$set": {"brothers": list}}, upsert=True)
    else:
        await brothersdb.insert_one({"b1_id": b1_id}, {"$set": {"brothers": [b2_id]}})


async def del_sister(b1_id: int, b2_id: int):
    x = await brothersdb.find_one({"b1_id": b1_id})
    if x:
        list = x["brothers"]
        if b2_id in list:
            list.remove(b2_id)
            await brothersdb.delete_one({"b1_id": b1_id}, {"$set": {"brothers": list}}, upsert=True)

async def are_sisters(s1_id: int, s2_id: int):
    x = await sistersdb.find_one({"s1_id": s1_id})
    if x:
        list = x["sisters"]
        if s2_id in list:
            return True
    return False

async def get_brothers(b1_id):
    x = await brothersdb.find_one({"b1_id": b1_id})
    if not x:
        return []
    else:
        list = x["brothers"]
        return list
