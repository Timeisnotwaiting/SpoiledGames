from Database.sisters import *
from Database.brothers import *
from Spl import get_id

@Client.on_message(filters.command("sibling"))
async def sibling(_, m):
    s1_id = m.from_user.id
    s2_id = await get_id(_, m) 
    
    
