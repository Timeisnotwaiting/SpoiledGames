async def get_id(_, m):
    if m.reply_to_message:
        id = m.from_user.id
    elif len(m.command) > 1:
        txt = m.text.split()
        if txt[1][0] == "@":
            id = (await _.get_users(txt[1])).id
        else:
            id = int(txt[1])
    return id
