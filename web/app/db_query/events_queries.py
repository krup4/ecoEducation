
# SQL INJECTION ALERT 🚨🚨🚨🚨🚨🚨
def insert_event(uuid, time, adress, name, cost, tags, description):
    right_tags = '[ '
    for el in tags:
        right_tags += f'"{el}", '
    right_tags = right_tags[:-2:]
    right_tags += ' ]'
    return f"INSERT INTO events (uuid, time, adress, name, cost, tags, description) VALUES ('{uuid}', '{time}', '{adress}', '{name}', {cost}, '{right_tags}', '{description}')"


def delete_event(uuid):
    return f"DELETE FROM events WHERE uuid = '{uuid}'"


def edit_event(uuid, data):
    query = "UPDATE events SET "
    print(data)
    for key, value in data.items():
        print(key, value)
        if key != "uuid" and key != "tags":
            query += f"{key} = '{value}', "
        if key == "tags":
            right_tags = '[ '
            for el in value:
                right_tags += f'"{el}", '
            right_tags = right_tags[:-2:]
            right_tags += ' ]'
            query += f"{key} = '{right_tags}', "

    query = query[:-2:] + f" WHERE uuid = '{uuid}'"

    return query
