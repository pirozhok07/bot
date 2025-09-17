import crud

async def create_user(*,
                      user_id: int,
                      full_name: str,
                      username:str):
    user = await crud.get_user(user_id)
    if not user:
        await crud.create_user(user_id, full_name, username)
        return True
    return False
