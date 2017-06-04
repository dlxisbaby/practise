#coding:utf-8

import socket
import threading

def clientThreadIn(conn,nick):
    global data
    while True:
        try:
            temp = conn.recv(1024)
            if not temp:
                conn.close()
                return
            NotifyAll(temp)
            print data
        except:
            NotifyAll(nick+"leave the room")
            print data
            return
        
def clientThreadOut(conn,nick):
    global data
    while True:
        if con.acquire():
            con.wait()
            if data:
                try:
                    conn.send(data)
                    con.release()
                except:
                    con.release()
                    return

def NotifyAll(ss):
    global data
    if con.acquire():
        data = ss
        con.notifyAll()
        con.release()

con = threading.Condition() #条件
HOST = raw_input("input IP address:")
port = 8888
data = ''

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)    #创建socket
print "socket created"
s.bind((HOST,port)) #把socket绑定到IP地址
s.listen(5)
print "socket now listening"

while True:
    conn,addr = s.accept() #接收连接
    print addr[0]+":"+str(addr[1])+" connected"
    nick = conn.recv(1024) #获取用户名
    NotifyAll("welcome "+nick+" to the room")
    print data
    print str((threading.activeCount()+1) / 2) + "person(s)"
    conn.send(data)
    threading.Thread(target=clientThreadIn,args=(conn,nick)).start()
    threading.Thread(target=clientThreadOut,args=(conn,nick)).start()
    
    
    