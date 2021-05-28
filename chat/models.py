# from django.db import models
# from django.conf import settings
#
# class ChatRoom(models.Model):
#     title = models.CharField(max_length=50, unique=True, blank=False)
#     users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, help_text='users who are connected')
#
#     def __str__(self):
#         return self.title
#
#     def connect_user(self, user):
#         is_user_added = False
#         if not user in self.users.all():
#             self.users.add(user)
#             self.save()
#             is_user_added = True
#         elif user in self.users.all():
#             is_user_added = True
#         return is_user_added
#
#     def disconnect_user(self, user):
#         is_user_removed = False
#         if user in self.users.all():
#             self.users.remove(user)
#             self.save()
#             is_user_removed = True
#
#         return is_user_removed
#
#     @property
#     def group_name(self):
#         return f"PublicChatRoom-{self.id}"
#
#
# class PublicChatRoomManager(models.Model):
#     def by_room(self, room):
#         qs = PublicChatRoomMessage.objects.filter(room=room).order_by('-timestamp')
#         return qs
#
#
# class PublicChatRoomMessage(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     room =models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
#     timestamp = models.DateTimeField(auto_now_add=True)
#     content = models.TextField(unique=False, blank=False)
#
#     def __str__(self):
#         return self.content


from django.db import models

class Message(models.Model):
    username = models.CharField(max_length=255)
    room = models.CharField(max_length=255)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)