# coding=gbk
#---- Condition
#---- ׽�Բص���Ϸ
import threading, time
class Seeker(threading.Thread):
    def __init__(self, cond, name):
        super(Seeker, self).__init__()
        self.cond = cond
        self.name = name
    
    def run(self):
        time.sleep(1) #ȷ��������Seeker�еķ���   
        
        self.cond.acquire() #b    
        print self.name + ': ���Ѿ����۾�������'
        self.cond.notify()
        self.cond.wait() #c    
                         #f 
        print self.name + ': ���ҵ����� ~_~'
        self.cond.notify()
        self.cond.release()
                            #g
        print self.name + ': ��Ӯ��'   #h
        
class Hider(threading.Thread):
    def __init__(self, cond, name):
        super(Hider, self).__init__()
        self.cond = cond
        self.name = name
    def run(self):
        self.cond.acquire()
        self.cond.wait()    #a    #�ͷŶ�����ռ�ã�ͬʱ�̹߳��������ֱ����notify������ռ������
                            #d
        print self.name + ': ���Ѿ��غ��ˣ���������Ұ�'
        self.cond.notify()
        self.cond.wait()    #e
                            #h
        self.cond.release() 
        print self.name + ': �����ҵ��ˣ���~~~'
        
cond = threading.Condition()
seeker = Seeker(cond, 'seeker')
hider = Hider(cond, 'hider')
seeker.start()
hider.start()