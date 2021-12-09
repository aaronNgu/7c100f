def get_help():
    print("inside get help")


def count_unread_messages(message_dicts, user_id):
    """Count the number of message unread by user_id. 
    A message dict contians key {id, text, senderId, createdAt, isRead}"""
    print("counting unread messages")
    messages_for_user = filter(
        lambda message: message["senderId"] != user_id, message_dicts)
    unread_messages = filter(
        lambda message: not message["isRead"], messages_for_user)
    return len(list(unread_messages))


def set_is_last_read(message_dicts, user_id):
    """Assume the messages are sorted by from the oldest to latest,
    add the field '["is_last_read"] = True' to the last message 
    read by user in the conversation.
    A message dict contians key {id, text, senderId, createdAt, isRead}"""
    for message in reversed(message_dicts):
        if message["isRead"]:
            message["isLastRead"] = True
            break
