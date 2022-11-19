from . import db

sistersdb = db.sisters

async def add_sister(s1_id: int, s2_id: int):
    x = await sistersdb.find_one({"s1_id": s1_id})
    if x:
        list = x["sisters"]
        if not s2_id in list:
            list.append(s2_id)
            return await sistersdb.update_one({"s1_id": s1_id}, {"$set": {"sisters": list}}, upsert=True)
    else:
        await sistersdb.insert_one({"s1_id": s1_id}, {"$set": {"sisters": [s2_id]}})


async def del_sister(s1_id: int, s2_id: int):
    x = await sistersdb.find_one({"s1_id": s1_id})
    if x:
        list = x["sisters"]
        if s2_id in list:
            list.remove(s2_id)
            await sistersdb.delete_one({"s1_id": s1_id}, {"$set": {"sisters": list}}, upsert=True)

async def is_sister(s1_id: int, s2_id: int):
    x = await sistersdb.find_one({"s1_id": s1_id})
    if x:
        list = x["sisters"]
        if s2_id in list:
            return True
    return False

async def get_sisters(s1_id):
    x = await sistersdb.find_one({"s1_id": s1_id})
    if not x:
        return []
    else:
        list = x["sisters"]
        return list
