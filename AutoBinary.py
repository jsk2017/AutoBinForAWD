# -*- coding:utf-8 -*-
import argparse
import os 
import sys
# from ssh_interface import *
from  autoUtil  import *
def main():
    parser = argparse.ArgumentParser()

    #Add arguments
    parser.add_argument('--dump',help="To dump binary source",action='store_true')
    parser.add_argument('--find',help="To get the pathslist of flag",action="store_true")
    parser.add_argument('--get',help="To dump choose file from remote host,but if you want get without losting privilege you prefect using [scp -P user@hostname:remote_file local_file] to get file",action="store_true")
    parser.add_argument('--put',help="To put choose file to remote host，but if you want put without losting privilege you prefect using [scp -P port local_file user@hostname:remote_file] to put file",action="store_true")

    parser.add_argument('-c','--command',help="To exec command by ssh")

    parser.add_argument('-ip', '--hostname',help="Input remote hostname[ip]")
    parser.add_argument('-P', '--port',help="Input remote ssh or sftp port")
    parser.add_argument('-u', '--username',help="Input remote ssh username")
    parser.add_argument('-p', '--passwd',help="Input remote ssh passwd")
    parser.add_argument('-k', '--keyfile',help="Input ssh key file")
    
    parser.add_argument('-r', '--remotepath',help="Input remotepath file name to dump or overwrite it")
    parser.add_argument('-l', '--localpath',help="Input localpath file name ")
    parser.add_argument('-v','--version',help='Edit by BadRer V1.0',action="store_true")


    #Parse Arguments
    args =parser.parse_args()

    #Print version infomation
    if args.version:
        print '''
__________             ._____________              
\______   \_____     __| _/\______   \ ___________ 
 |    |  _/\__  \   / __ |  |       _// __ \_  __ \
 |    |   \ / __ \_/ /_/ |  |    |   \  ___/|  | \/
 |______  /(____  /\____ |  |____|_  /\___  >__|   
        \/      \/      \/         \/     \/       


[+] Version 1.0 Edit by BadRer!'''
        exit(0)

    #Check for arguments error:
    if not args.hostname or not args.port or not args.username or (not args.passwd and not args.keyfile):
        print "[-] Error! Please input base ssh connection info"
        exit(0)


    a=args.dump
    b=args.find
    c=args.get
    d=args.put
    e=args.command
    flag = (a and not b and not c and not d and not e) or (not a and not b and not c and d and not e) or (not a and not b and c and not d and not e) or (not a and b and not c and not d and not e) or (not a and not b and not c and not d and e)
    if not flag:
        print "[-] Error! Please input one args of ['--dump' '--find' '--get' '--put' '--command']"
    print "Test ok"
    if args.dump :
        ssh_dump(args.hostname,args.port,args.username,args.passwd,args.keyfile)
    elif args.find :
        ssh_find(args.hostname,args.port,args.username,args.passwd,args.keyfile)
    elif args.get :
        ssh_get(args.hostname,args.port,args.username,args.passwd,args.keyfile,args.remotepath,args.localpath)
    elif args.put :
        ssh_put(args.hostname,args.port,args.username,args.passwd,args.keyfile,args.localpath,args.remotepath)
    elif args.command:
        ssh_exec(args.hostname,args.port,args.username,args.passwd,args.keyfile,args.command)

    

main()



'''
大致思路：
获取用户参数
--dump   to dump binary source
--find   to get path of flag
--get    to dump choose file from remote host
--put    to put choose file to remote host
--cmd    to exec command by ssh

--hostname '192.168.43.252' --port 22 --username 'pwn' --passwd '123' --dump
--hostname '192.168.43.252' --port 22 --username 'pwn' --passwd '123' --find
--hostname '192.168.43.252' --port 22 --username 'pwn' --passwd '123' --get --remotepath '/home/username/xxx' --localpath 'xxx'
--hostname '192.168.43.252' --port 22 --username 'pwn' --passwd '123' --put --remotepath '/home/username/xxx' --localpath 'xxx' 
--hostname '192.168.43.252' --port 22 --username 'pwn' --passwd '123' --cmd 'ls'

--dump       == -d
--hostname   == -h
--port       == -P
--username   == -u
--passwd     == -p
--remotepath == -r
--localpath  == -l

'''
