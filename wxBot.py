from wxauto import *
import json
import time
import schedule
from revChatGPT import Chatbot

with open("config.json", "r", encoding='utf-8') as f:
    config = json.load(f)
chatbot = Chatbot(config)
chatbot.refresh_session()

# 获取当前微信客户端
wx = WeChat()

friendsList = [] #定义好友列表,用于指定用ai可以回复哪些好友的信息不指定则回复所有好友消息

def recWeChatMsg():
    clist = friendsList
    if(len(clist)==0):
        clist = wx.GetSessionList()
    for name in clist:
        wx.ChatWith(name)
        msgs = wx.GetLastMessage
        lastMsgUser = msgs[0]
        #最后一条信息不为自己发出时，调用chatgpt
        if(lastMsgUser != 'yvld' and lastMsgUser != 'SYS'):
            print('读取到 %s : %s'%(msgs[0], msgs[1]))
            msg = msgs[1]
            sendChatGPT(msg,lastMsgUser)


def openChatWindow(name):
    wx.ChatWith(name)

def sendChatGPT(question,name):
    openChatWindow(name)
    message = chatbot.get_chat_response(question)

    wx.SendMsg(message['message'])

schedule.every().second.do(recWeChatMsg)

while True:
    schedule.run_pending()  # 运行所有可以运行的任务
    time.sleep(1)