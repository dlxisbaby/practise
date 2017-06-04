#coding:utf-8

import socket
import threading

outString = ''
inString = ''
nick = ''

#发送信息的方法
def DealOut(sock):
    global nick,outString
    while True:
        outString = raw_input()
        outString = nick+":"+outString
        sock.send(outString)

#接收信息的方法
def DealIn(sock):
    global inString
    while True:
        try:
            inString = sock.recv(1024)
            if not inString:
                break
            if outString != inString:
                print inString
        except:
            break    

#手动输入用户名和IP地址
nick = raw_input("input nick name:")
ip = raw_input("input ip address:")

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #创建socket
sock.connect((ip,8888)) #发起请求
sock.send(nick)

#使用多线程，一个线程接收信息，一个发送信息
thin = threading.Thread(target=DealIn,args=(sock,))   #创建接收信息的线程
thin.start()
thout = threading.Thread(target=DealOut,args=(sock,))  #创建发送信息的线程
thout.start()


