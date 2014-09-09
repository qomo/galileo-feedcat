#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from weibo import APIClient
import time 
import threading 
from pyGalileo import *

class WeiBo(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.thread_stop = False
        self.APP_KEY='792490047'
        self.APP_SECRET='ce419042c4a2bc68094bd80f77b974e6'
        self.CALLBACK_URL = 'https://api.weibo.com/oauth2/default.html'
        self.client = APIClient(app_key=self.APP_KEY,app_secret=self.APP_SECRET, redirect_uri=self.CALLBACK_URL)
        self.access_token=u'2.009mf6fF0XrMdr167233bd6fcC1H4E'
        self.expires_in=1136006746
        self.client.set_access_token(self.access_token, self.expires_in)
        self.renew_old_mentions_number()
        self.OLD_MENTIONS_NUM = self.OLD_MENTIONS_NUM - 1
    
    def send_txt(self, string=u"Hello World!"):
        self.client.statuses.update.post(status=string)

    def send_img(self, figure, string='Default Text!!!'):
        self.client.statuses.upload.post(status=string, pic=figure)
    
    def get_mentions_number(self):
        return self.client.statuses.mentions.get().total_number

    def renew_old_mentions_number(self):
        self.OLD_MENTIONS_NUM = self.get_mentions_number()

    def get_new_mentions(self):
        r = self.client.statuses.mentions.get()
        num_mentions = r.total_number
        num_new_mentions = num_mentions - self.OLD_MENTIONS_NUM
        return r.statuses[0:num_new_mentions]

#    def get_latest_mention(self):
#        r = self.client.statuses.mentions.get()
#        return r.statuses[0]
#
#    def get_latest_mention_text(self):
#        latest_statuse = self.get_latest_mention()
#        return latest_statuse.text
#
#    def get_latest_mention_uid(self):
#        latest_statuse = self.get_latest_mention()
#        return latest_statuse.user.id
#
#    def get_latest_mention_time(self):
#        latest_statuse = self.get_latest_mention()
#        return latest_statuse.created_at

    def run(self):
        while not self.thread_stop:
            time.sleep(2)
            for st in self.get_new_mentions():
#                print isinstance(st.text, unicode)
#		print u"\u6d4b\u8bd5" in st.text
		print st.text.encode('utf-8')
                #print st
            self.renew_old_mentions_number()

    def stop(self):
        self.thread_stop = True


class DigitalPin:
    '''example irdetecter = DigitalPin(4, INPUT)'''
    def __init__(self, pnum, direction):
        '''init the DigitalPin:
            pnum --- DigitalPin number
            direction --- INPUT or OUTPUT
            '''
        self.PNUM=pnum
        pinMode(pnum, direction)

    def get_state(self):
        if direction==HIGH:
            return digitalRead(self.PNUM)
        else:
            print "ERROR!!!"

    def set_state(self, val):
        if direction==LOW:
            digitalWrite(self.PNUM, val)
        else:
            print "ERROR!!!"



if __name__=="__main__":
    wb=WeiBo()
    wb.start()
    time.sleep(3)
    wb.stop()
    #wb.send_txt(u'Hello feetcat!')
    #f = open('./yeelink.jpg', 'rb')
    #wb.send_img(figure=f)
    #f.close()
