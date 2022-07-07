from .. import db
filters = db.filters


def add_filters(keyword, chat_id, message_id) -> None:
    try:
        add = filters.find_one({"keyword": keyword})
    except TypeError:
        filters.insert_one(
            {"keyword": keyword, "chat_id": chat_id, "msg_id": message_id}
        )
    if add:
        filters.update_one(
            {"keyword": keyword},
            {"$set": {"chat_id": chat_id, "msg_id": message_id}},
        )
    else:
        filters.insert_one(
            {"keyword": keyword, "chat_id": chat_id, "msg_id": message_id}
        )


def del_filters(keyword, chat_id):
    filters.delete_one({"keyword": keyword, "chat_id": chat_id})


def filters_info(keyword, chat_id):
    r = filters.find_one({"keyword": keyword, "chat_id": chat_id})
    if r:
        return r
    else:
        return False


def filters_del(chat_id):
    filters.delete_many({"chat_id": chat_id})


def all_filters(chat_id):
    all = []
    for a in filters.find({"chat_id": chat_id}):
        all.append(a)
    if len(all) > 0:
        return all
    else:
        return False
