# Generated by Django 3.2 on 2021-05-28 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_alter_chatroom_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('room', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('date_added',),
            },
        ),
        migrations.RemoveField(
            model_name='chatroom',
            name='users',
        ),
        migrations.DeleteModel(
            name='PublicChatRoomManager',
        ),
        migrations.RemoveField(
            model_name='publicchatroommessage',
            name='room',
        ),
        migrations.RemoveField(
            model_name='publicchatroommessage',
            name='user',
        ),
        migrations.DeleteModel(
            name='ChatRoom',
        ),
        migrations.DeleteModel(
            name='PublicChatRoomMessage',
        ),
    ]
