

from fbchat import log, Client
from fbchat.models import *

        


 
class EchoBot(Client):
    def onMessage(self, author_id, message, thread_id, thread_type, **kwargs):
        if author_id != self.uid:
            log.info('Nhan tin nhan tu {} noi dung la: {}'.format(author_id,message))
        
        if author_id != self.uid:
           
            messe = kernel.respond(message)
            
            self.sendMessage(messe,thread_id=thread_id,thread_type=thread_type)
 


client = EchoBot('ntnytcpl@gmail.com','516489C@k')
client.listen()
