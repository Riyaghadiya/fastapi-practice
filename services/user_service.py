users = {}
next_user_id = 1


def create_user(user_data):
    global next_user_id

    user = user_data.model_dump()
    user["id"] = next_user_id

    users[next_user_id] = user
    next_user_id += 1

    return user


def get_all_users():
    return list(users.values())


def get_user_by_id(user_id):
    return users.get(user_id)


def update_user(user_id, user_data):
    if user_id not in users:
        return None

    updated_user = user_data.model_dump()
    updated_user["id"] = user_id

    users[user_id] = updated_user

    return updated_user


def delete_user(user_id):
    if user_id not in users:
        return False

    del users[user_id]
    return True