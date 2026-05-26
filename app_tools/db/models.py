import uuid
from datetime import datetime

from peewee import *

from .db import db


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    id = PrimaryKeyField(default=uuid.uuid4, unique=True)
    username = CharField(unique=True)
    password = CharField()
    security_question = CharField(null=True)
    security_answer = CharField(null=True)
    created_at = DateTimeField(default=datetime.now)


class HiddenFile(BaseModel):
    TYPE_CHOICES = [
        ('image', 'image'),
        ('video', 'video'),
        ('audio', 'audio'),
        ('document', 'document'),
    ]
    user = ForeignKeyField(User)
    id = PrimaryKeyField(default=uuid.uuid4, unique=True)
    filename = CharField()
    file_extension = CharField()
    file_type = CharField(choices=TYPE_CHOICES)
    file_size = IntegerField(default=0)
    path = CharField()
    original_path = CharField()
    date_created = DateTimeField(default=datetime.now)


class HiddenAudioFile(HiddenFile):
    author = CharField(default='unknown author')
    name = CharField()
    album_name = CharField(null=True)
    album_artist = CharField(null=True)
    composer = CharField(null=True)
    track_number = IntegerField(null=True)


class Login(BaseModel):
    user = ForeignKeyField(User)
    login_time = DateTimeField(default=datetime.now)
