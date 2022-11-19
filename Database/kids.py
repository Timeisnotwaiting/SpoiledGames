from . import db

kidsdb = db.kids

async def add_kid(p_id: int, k_id: int):
    x = await kidsdb.find_one({"p_id": p_id})
    if x:
        list = x["kids"]
        list.append(k_id)
        return await kidsdb.update_one({"p_id": p_id}, {"$set": {"kids": list}}, upsert=True)
    else:
        list = [k_id]
        return await kidsdb.update_one({"p_id": p_id}, {"$set": {"kids": list}}, upsert=True)

async def del_kid(p_id: int, k_id: int):
    x = await kidsdb.find_one({"p_id": p_id})
    if x:
        list = x["kids"]
        list.remove(k_id)
        return await kidsdb.update_one({"p_id": p_id}, {"$set": {"kids": list}}, upsert=True)

async def is_kid(p_id: int, k_id: int):
    x = await kidsdb.find_one({"p_id": p_id})
    if x:
        list = x["kids"]
        if k_id in list:
            return True
    return False

async def get_kids(p_id: int):
    x = await kidsdb.find_one({"p_id": p_id})
    if x:
        list = x["kids"]
        return list
    return []
