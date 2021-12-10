from django.contrib.auth.middleware import get_user
from django.http import HttpResponse, JsonResponse
from messenger_backend.models import Conversation, Message
from rest_framework.views import APIView
from rest_framework.request import Request
from messenger_backend.utils.conversation_helper import set_is_last_read

class SingleConversation(APIView):

    def put(self, request: Request):
        """expects {conversationId} mark isRead to True 
        for all messages where current user is not the sender. 
        returns the {conversationId, messages}"""
        try:
            user = get_user(request)

            if user.is_anonymous:
                return HttpResponse(status=401)
            user_id = user.id

            conversation_id = request.data.get("conversationId")
            # converastion id must be int
            if type(conversation_id) is not int:
                return HttpResponse(status=404)
            convo = Conversation.objects.get(id=conversation_id)
            # conversation doesn't exists
            if not convo:
                return HttpResponse(status=404)

            # Mark isRead for all messages read by current user
            messages = Message.objects.filter(conversation=convo).order_by("createdAt")
            messages_for_user = messages.exclude(senderId=user_id)
            unread_messages_for_user = messages_for_user.filter(isRead=False)
            unread_messages_for_user.update(isRead=True)

            messages = [message.to_dict(
                ["id", "text", "senderId", "createdAt", "isRead"])
                for message in messages.all()]

            # set isLastRead flag for message that was last read by current user
            # these messages will be sent to the other user through socket
            set_is_last_read(messages, user_id)

            return JsonResponse(
                {"conversationId": conversation_id,
                    "messages": messages},
                safe=False,
            )
        except Exception as e:
            return HttpResponse(status=500)
