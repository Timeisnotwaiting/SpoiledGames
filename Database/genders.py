from . import db

genderdb = db.gender

async def check_gender(id: int):
    x = await genderdb.find_one({"id": id})
    if x:
        return "female"
    return "male"

async def change_gender(id: int):
    x = await genderdb.find_one({"id": id})
    if x:
        return await genderdb.delete_one({"id": id})
    return await genderdb.insert_one({"id": id})
