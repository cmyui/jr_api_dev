import services
import utils.security


async def create_user(email: str, first_name: str, password: str):
    query = """
        INSERT INTO users (email, first_name, password)
             VALUES (:email, :first_name, :password)
    """
    values = {
        "email": email,
        "first_name": first_name,
        "password": utils.security.hash_password(password),
    }
    user_id = await services.database.execute(query, values)

    query = """
        SELECT id, email, first_name
          FROM users
         WHERE id = :user_id
    """
    values = {
        "user_id": user_id,
    }
    user_row = await services.database.fetch_one(query, values)
    return user_row


async def get_user(user_id: int):
    query = """
        SELECT id, email, first_name
          FROM users
         WHERE id = :user_id
    """
    values = {
        "user_id": user_id,
    }
    user_row = await services.database.fetch_one(query, values)
    return user_row
