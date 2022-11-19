from . import db

parentsdb = db.parents

async def add_parent(k_id: int, p_id: int):
    x = await parentsdb.find_one({"k_id": k_id})
    if x:
        list = x["parents"]
        list.append(p_id)
        return await parentsdb.update_one({"k_id": k_id}, {"$set": {"parents": list}}, upsert=True)
    else:
        list = [p_id]
        return await parentsdb.update_one({"k_id": k_id}, {"$set": {"parents": list}}, upsert=True)

async def del_parent(k_id: int, p_id: int):
    x = await parentsdb.find_one({"k_id": k_id})
    if x:
        list = x["parents"]
        list.remove(p_id)
        return await parentsdb.update_one({"k_id": k_id}, {"$set": {"parents": list}}, upsert=True)

async def is_parent(k_id: int, p_id: int):
    x = await parentsdb.find_one({"k_id": k_id})
    if x:
        list = x["parents"]
        if p_id in list:
            return True
    return False

async def get_parents(k_id: int):
    x = await parentsdb.find_one({"k_id": k_id})
    if x:
        list = x["parents"]
        return list
    return []
