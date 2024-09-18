def insert_event(time, latitude, longitude, name, cost, tags, description):
    return f"INSERT INTO users (time, latitude, longitude, name, cost, tags, description) VALUES ('{time}', '{latitude}', '{longitude}', '{name}', {cost}, '{tags}', '{description}')"


def delete_event(uid):
    pass
