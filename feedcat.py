#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from weibo import APIClient
import time 
import threading 
from pyGalileo import *

class WeiBoRobot(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.thread_stop = False
        self.APP_KEY='xxxxxx'
        self.APP_SECRET='xxxxxxxxxxxxxxxxxxx'
        self.CALLBACK_URL = 'https://api.weibo.com/oauth2/default.html'
        self.client = APIClient(app_key=self.APP_KEY,app_secret=self.APP_SECRET, redirect_uri=self.CALLBACK_URL)
        self.access_token=u'x.xxxxxxxxxxxxxx'
        self.expires_in=xxxxxxxxxxxxxxxxx
        self.client.set_access_token(self.access_token, self.expires_in)
        self.renew_old_mentions_number()
        # self.OLD_MENTIONS_NUM = self.OLD_MENTIONS_NUM - 4
        self.door = FoodDoor(7, 8, 6)
    
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

    def push_img(self, string=u'喵喵,耶！'):
        os.system("fswebcam -d /dev/video0 -r 320x240 --bottom-banner --title 'Galileo Feed Cat' --no-timestamp ./capture.jpg")
        # time.sleep(1)
        f = open('./capture.jpg', 'rb')
        self.send_img(f, string)
        f.close()

    def run(self):
        while not self.thread_stop:
            time.sleep(5)
            new_mentions = self.get_new_mentions()
            new_mentions.reverse()
            for st in new_mentions:
                print st.text.encode('utf-8')
                if u'\u732b\u54aa\u5403' in st.text:    # 猫咪吃
                    self.door.feedCat()
                    self.push_img("好吃，谢谢主人，喵喵！")
                if u'\u4e00\u4e8c\u4e09\u5494\u5693' in st.text: # 一二三咔嚓
                    self.push_img("茄子！")
                if u'\u6491\u6b7b\u4e86' in st.text:    # 撑死了
                    self.stop()
            self.renew_old_mentions_number()

    def stop(self):
        self.thread_stop = True


class PIRSensor(threading.Thread):
    """用于控制热释红外传感器"""
    def __init__(self, sensorPin):
        threading.Thread.__init__(self)
        self.thread_stop = False
        self.wb = WeiBoRobot()
        self.is_feeding = False
        self.sensorPin = sensorPin
        pinMode(sensorPin, INPUT)
        self.door = FoodDoor(7, 8, 6)

    def isCatHere(self):
        if digitalRead(self.sensorPin)==HIGH:
            return True
        else:
            return False

    def run(self):
        time.sleep(2)
        while not self.thread_stop:
            if self.isCatHere():
                self.door.feedCat()
                self.wb.push_img("自己找食，丰衣足食……喵!")
                time.sleep(600)

    def stop(self):
        self.thread_stop = True

class FoodDoor:
    """控制门控电机"""
    def __init__(self, motorpin1, motorpin2, clossdoorpin):
        self.motorpin1 = motorpin1
        self.motorpin2 = motorpin2
        self.clossdoorpin = clossdoorpin
        pinMode(motorpin1, OUTPUT)
        pinMode(motorpin2, OUTPUT)
        pinMode(clossdoorpin, INPUT)

    def openDoor(self):
        digitalWrite(self.motorpin1, HIGH)
        digitalWrite(self.motorpin2, LOW)

    def closeDoor(self):
        digitalWrite(self.motorpin1, LOW)
        digitalWrite(self.motorpin2, HIGH)

    def stopDoor(self):
        digitalWrite(self.motorpin1, LOW)
        digitalWrite(self.motorpin2, LOW)

    def isClose(self):
        return digitalRead(self.clossdoorpin)

    def autoCloseDoor(self):
        self.closeDoor()
        while self.isClose()==LOW:
            self.is_close = self.isClose()
            time.sleep(0.05)
        self.stopDoor()

    def openDoorTime(self, seconds):
        self.openDoor()
        time.sleep(seconds)
        self.stopDoor()

    def feedCat(self):
        self.openDoorTime(0.15)
        time.sleep(0.3)
        self.autoCloseDoor()


if __name__=="__main__":
    wb=WeiBoRobot()
    wb.start()
    autoFeed = PIRSensor(5)
    autoFeed.start()
    while 1:
        isquit = raw_input("Input 'q' to stop program:\n")
        if isquit == 'q':
            wb.stop()
            autoFeed.stop()
            break
    # time.sleep(4)
    # wb.stop()
    #wb.send_txt(u'Hello feedcat!')
    #f = open('./yeelink.jpg', 'rb')
    #wb.send_img(figure=f)
    #f.close()
    # dr = FoodDoor(7, 8, 6)
    # dr.openDoorTime(0.1)
    # dr.closeDoor()
    # time.sleep(0.3)
    # dr.autoCloseDoor()
    # dr.stopDoor()
