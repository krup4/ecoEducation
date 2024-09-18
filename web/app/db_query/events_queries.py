def insert_event(time, uuid, adress, name, cost, tags, description):
    return f"INSERT INTO events (time, latitude, longitude, name, cost, tags, description) VALUES ('{uuid}', '{time}', '{adress}', '{name}', {cost}, '{tags}', '{description}')"


def delete_event(uuid):
    return f"DELETE FROM events WHERE uuid = '{uuid}'"

def edit_event(uuid, data):
    query = "UPDATE events SET "
    for key, value in data:
        query += f"{key} = '{value}', "
    
    query = query[:-2:] + f" WHERE uuid = '{uuid}'"

    return query
