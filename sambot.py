from getpass import get_pass
from fbchat import Client, Message
from random import choice
import json

class Account(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        responses = []
        with open('responses.json', 'r') as file1:
            file1_json = json.load(file1)
            responses = list(file1_json["responses"])
        message = 'sambar'
        sentMessage = None
        toggle = self.fetchThreadMessages(thread_id, 1, None)
        for elem in toggle:
            sentMessage = elem
            break
        try:
            sentMessage = sentMessage.lower()
        except AttributeError:
            sentMessage = sentMessage.text.lower()
        #self.login('email',get_pass())
        if message in sentMessage and author_id != client.uid:
            self.send(Message(choice(responses)), thread_id, thread_type)
            self.markAsDelivered(author_id, thread_id)
        #self.logout()
        #self.stopListening()

client = Account('email', get_pass())

while True:
    client.login('email',get_pass())
    client.listen()
    try:
        client.logout()
    except AttributeError:
        client.stopListening()