import datetime
import time
import uuid

from peewee import *
from .db import db


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    id = PrimaryKeyField(default=uuid.uuid4, unique=True)
    username = CharField(unique=True)
    password = CharField()
    security_question = CharField()
    security_answer = CharField()


class HiddenFile(BaseModel):
    TYPE_CHOICES = [
        ('image', 'image'),
        ('video', 'video'),
        ('audio', 'audio'),
        ('document', 'document'),
    ]
    id = PrimaryKeyField(default=uuid.uuid4, unique=True)
    filename = CharField()
    file_extension = CharField()
    file_type = CharField(choices=TYPE_CHOICES)
    file_size = IntegerField(default=0)
    path = CharField()
    original_path = CharField()
    date_created = DateTimeField(default=datetime.datetime.now)


class HiddenAudioFile(HiddenFile):
    author = CharField(default='unknown author')
    name = CharField()
    album_name = CharField(null=True)
    album_artist = CharField(null=True)
    composer = CharField(null=True)
    track_number = IntegerField(null=True)


