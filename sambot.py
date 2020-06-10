from getpass import get_pass
from fbchat import Client, Message
from random import choice
import json

class Account(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        pass


client = Account('email', get_pass())
client.send(Message('we need sambar'), thread_id, ThreadType.USER)