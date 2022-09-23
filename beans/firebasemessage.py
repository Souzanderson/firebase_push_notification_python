import firebase_admin
from firebase_admin import messaging
from firebase_admin import credentials


class MessagePushNotification:
    def __init__(self, topic, title="C4Action", body="Existem Linhas com ocorrências aguardando..."):
        self.topic = topic
        self.title = title
        self.body = body

    @property
    def message(self):
        return messaging.Message(
            notification=messaging.Notification(
                title=self.title,
                body=self.body
            ),
            topic=self.topic
        )

class PushNotification:
    def __init__(self, message_agent:MessagePushNotification, credentials_location = "firebase_key.json"):
        self.__message_agent = message_agent
        self.__credentials = credentials_location
        self.__authenticate__()
        
    
    def __authenticate__(self):
        cred = credentials.Certificate(self.__credentials)
        try: firebase_admin.get_app()
        except: firebase_admin.initialize_app(cred) 
        
    
    def send(self):
        messaging.send(self.__message_agent.message)
