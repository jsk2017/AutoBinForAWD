# -*- coding:utf-8 -*-

from pwn import *
from autoUtil import auto_get_submit
from multiprocessing import Pool

import os
import random
import threading
import request
import time
import sys
import signal



class myThread (threading.Thread):   #继承父类threading.Thread
    def __init__(self, hostname, port, delay):
        threading.Thread.__init__(self)
        self.hostname = hostname
        self.port = port
        self.delay = delay
    def run(self):                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数 
        while True:
            print "[ %s ] Starting Attack [ %s ] [ %s ]" % (time.ctime(time.time()),self.hostname,self.port) 
            try:
                auto_get_submit(self.hostname, self.port)
            except Exception as msg:
                print msg

            print "[ %s ] Attack is Done  [ %s ] [ %s ]" % (time.ctime(time.time()),self.hostname,self.port)
            print "[--------------------------------------------------]"
            time.sleep(self.delay)


def thread_batch_attack(iplist,port,delay):
    threads=[]
    # 创建新线程
    for ip in iplist:
        threads.append(myThread(ip,port,delay))


    # 开启线程
    for thread in threads:
        thread.start()


def multiprocess_batch_attack(iplist,port,delay):
    # def process_attack(ip,port,delay):
    #     while True:
    #         print "[ %s ] Starting multiprocess Attack [ %s ] [ %s ]" % (time.ctime(time.time()),ip,port) 
    #         try:
    #             auto_get_submit(ip, port)
    #         except Exception as msg:
    #             print msg
    #         print "[ %s ] Attack is Done  [ %s ] [ %s ]" % (time.ctime(time.time()),ip,port)
    #         print "[--------------------------------------------------]"
    #         time.sleep(delay)

    # p = Pool(2)
    # for ip in iplist:
    #     p.apply_async(process_attack, args=(ip,port,delay,))
    root = os.path.abspath('.')
    dirs = root+'/submit'
    print dirs
    if not os.path.exists(dirs):
        os.makedirs(dirs)
    
    templatePy = '''# -*- coding : utf-8 -*-
# file__name %s.py
import sys
import os
# add modul path
modul_path = os.path.abspath('.')
sys.path.append(modul_path)
# import handle function
from  autoUtil  import *
auto_get_submit('%s',%d) 
    '''
    templateBash = '''#/bin/bash
while true; do
    python %s >> %s
    sleep %ss
done
    '''
    try:
        # generate py & sh file
        commands = []
        for ip in iplist:
            sub_path = dirs+'/'+ip

            py_template_filename = sub_path+'/'+ip+'.py'
            sh_template_filename = sub_path+'/'+ip+'.sh'

            log_filename = sub_path+'/'+'log.txt'

            py_template = templatePy % (ip,ip,port)
            log_filename = sub_path+'/'+'log.txt'
            sh_template = templateBash % (py_template_filename,log_filename,delay)

            if not os.path.exists(sub_path):
                os.makedirs(sub_path)

            with open(py_template_filename,'w') as file:
                file.write(py_template)

            with open(sh_template_filename,'w') as file:
                file.write(sh_template)

            print "write Done!!"

            # ready to run
            command = 'nohup bash '+sh_template_filename
            # print command
            commands.append(command)
            # os.system(command)
            print 'Done'
            # print stdout.read()
            # os.system('cat /proc/cpuinfo')
        print commands
    except Exception as msg:
        print msg
        
    
if  __name__ == '__main__':
        
    iplist = ["192.168.43.252",'192.168.43.243']
    port = 10000
    delay = 5  # 120 s
    thread_batch_attack(iplist,port,delay)
    # multiprocess_batch_attack(iplist,port,delay)