import crud

async def create_user(*,
                      telegram_id: int,
                      full_name: str,
                      username:str):
    await crud.check_table_customer()
    user = await crud.get_user(telegram_id)
    if not user:
        await crud.create_user(telegram_id, full_name, username)
        return True
    return False
