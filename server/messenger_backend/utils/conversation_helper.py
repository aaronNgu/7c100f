def set_is_last_read(message_dicts, user_id):
    """Assumes the messages are sorted from the oldest to latest,
    add the field ["is_last_read"] = True to the last message 
    read by user in the conversation.
    A message dict contians key {id, text, senderId, createdAt, isRead}"""
    for message in reversed(message_dicts):
        if message["isRead"]:
            message["isLastRead"] = True
            break
