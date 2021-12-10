def count_unread_messages(message_dicts, user_id):
    """Count the number of user_id's unread messages. 
    A message dict contains key {id, text, senderId, createdAt, isRead}"""
    messages_for_user = filter(
        lambda message: message["senderId"] != user_id, message_dicts)
    unread_messages = filter(
        lambda message: not message["isRead"], messages_for_user)
    return len(list(unread_messages))


def set_is_last_read(message_dicts, user_id):
    """Assumes the messages are sorted from the oldest to latest,
    add the field ["is_last_read"] = True to the last message 
    read by user in the conversation.
    A message dict contians key {id, text, senderId, createdAt, isRead}"""
    for message in reversed(message_dicts):
        if message["isRead"]:
            message["isLastRead"] = True
            break
