from fbchat import log, Client
from fbchat.models import *
import botcalendar
import covid
import aiml
import os
import rncat,rndog,weather
from country import x

kernel = aiml.Kernel()
kernel.learn("start.xml")
kernel.respond("load aiml b")

class EchoBot(Client):
    def onMessage(self, author_id, message, thread_id, thread_type, **kwargs):
        if author_id != self.uid:
            log.info('Nhan tin nhan tu {} noi dung la: {}'.format(author_id,message))
 
        if author_id != self.uid:
            if message == "/tkb":
                if author_id == "100011339823838":
                    
                    self.sendMessage(botcalendar.main(),thread_id=thread_id,thread_type=thread_type)
                else:
                    eror = "Không có thông tin thời khóa biểu. Liên hệ: caophuoclong1@gmail.com"
                    self.sendMessage(eror,thread_id=thread_id,thread_type=thread_type)

            elif message == "/covid":

                self.sendMessage(covid.main("Vietnam"),thread_id=thread_id,thread_type=thread_type)
            elif message == "/cat":
                self.sendRemoteImage(rncat.main(),message="Gift For U <3",thread_id=thread_id,thread_type=thread_type)
            elif message == "/dog":
                self.sendRemoteImage(rndog.main(),message="Gift For U <3",thread_id=thread_id,thread_type=thread_type)
            elif message == "/country":
                self.sendMessage(x.main(self),thread_id=thread_id,thread_type=thread_type)
            elif message == "/weather":
                self.sendMessage(weather.main(),thread_id=thread_id,thread_type=thread_type)
            else :
                messe = kernel.respond(message)
                self.sendMessage(messe,thread_id=thread_id,thread_type=thread_type)


client = EchoBot('ntnytcpl@gmail.com','516489C@k')
client.listen()