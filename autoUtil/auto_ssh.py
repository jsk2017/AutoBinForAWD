#-*- coding:utf-8 -*-
import paramiko


# ssh 用户名 密码 登陆
def ssh_base_pwd(ip,port,username,passwd,cmd='ls'):
    port = int(port)
    ssh = paramiko.SSHClient()

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(hostname=ip, port=port, username=username, password=passwd)

    stdin,stdout,stderr = ssh.exec_command(cmd)

    result = stdout.read()
    if not result :
        result = stderr.read()
    ssh.close()
    
    return result.decode()


def ssh_pwd_print_result(ip,port,username,passwd,cmd='ls'):
    port = int(port)
    ssh = paramiko.SSHClient()

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(hostname=ip, port=port, username=username, password=passwd)

    stdin,stdout,stderr = ssh.exec_command(cmd)

    result = stdout.read()
    if not result :
        result = stderr.read()
    ssh.close()
    print result.decode().encode('gbk')# add new

    return result.decode().encode('gbk')


def ssh_pwd_get_flag_path(ip,port,username,passwd):
    try:
        cmd = 'find / -name flag.txt 2> /dev/null'
        flagtxt_paths = ssh_base_pwd(ip,port,username,passwd,cmd)
        print flagtxt_paths
    except Exception as msg:
        print msg
    try:
        cmd = 'find / -name flag 2> /dev/null'
        flag_path = ssh_base_pwd(ip,port,username,passwd,cmd)
        print flag_path
    except Exception as msg:
        print msg


# ssh 用户名 私钥 登陆
def ssh_base_keyfile(ip,port,username,keyfile,cmd='ls'):
    port = int(port)
    private_key = paramiko.RSAKey.from_private_key_file(keyfile)   #使用目标的私钥来登录
    ssh = paramiko.SSHClient()

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(hostname=ip, port=port, username=username, pkey=private_key)

    stdin,stdout,stderr = ssh.exec_command(cmd)

    result = stdout.read()
    if not result :
        result = stderr.read()
    ssh.close()
    
    return result.decode().encode('gbk')


def ssh_base_keyfile_print_result(ip,port,username,keyfile,cmd='ls'):
    port = int(port)
    private_key = paramiko.RSAKey.from_private_key_file(keyfile)   #使用目标的私钥来登录
    ssh = paramiko.SSHClient()

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(hostname=ip, port=port, username=username, pkey=private_key)

    stdin,stdout,stderr = ssh.exec_command(cmd)

    result = stdout.read()
    if not result :
        result = stderr.read()
    ssh.close()
    print result.decode().encode('gbk') # add new

    return result.decode().encode('gbk')


def ssh_base_keyfile_get_flag_path(ip,port,username,keyfile):
    
    try:
        cmd = 'find / -name flag.txt 2> /dev/null'
        flagtxt_paths = ssh_base_keyfile(ip,port,username,keyfile,cmd)
        print flagtxt_paths
    except Exception as msg:
        print msg
    try:
        cmd = 'find / -name flag 2> /dev/null'
        flag_path = ssh_base_keyfile(ip,port,username,keyfile,cmd)
        print flag_path
    except Exception as msg:
        print msg


## sftp 用户名 密码 登陆
def sftp_pwd(ip,port,username,passwd,remote_file,local_file,style):
    port = int(port)
    transport = paramiko.Transport((ip, port))
    transport.connect(username=username, password=passwd)
    sftp = paramiko.SFTPClient.from_transport(transport)

    if style == 'put':
        sftp.put(local_file, remote_file)  # 将123.py 上传至服务器 /tmp下并改名为test.py
    elif style == 'get':
        sftp.get(remote_file, local_file)  # 将remove_path 下载到本地 local_path

    transport.close()


def sftp_get_file(ip,port,username,passwd,remote_file,local_file):
    '''
    example --> scp username@ip:remote_file local_file
    '''
    try:
        sftp_pwd(ip,port,username,passwd,remote_file,local_file,style = 'get')
    except Exception as msg:
        print msg
    print "get [ %s ] is ok!" % remote_file


def sftp_put_file(ip,port,username,passwd,local_file,remote_file):
    '''
    example --> scp local_file username@ip:remote_file
    '''
    try:
        sftp_pwd(ip,port,username,passwd,remote_file,local_file,style = 'put')
    except Exception as msg:
        print msg
    print "put [ %s ] is ok!" % local_file


# sftp 用户名 私钥 登录
def sftp_keyfile(ip,port,username,keyfile,remote_file,local_file,style):
    port = int(port)
    private_key = paramiko.RSAKey.from_private_key_file(keyfile)

    transport = paramiko.Transport((ip, port))
    transport.connect(username=username, pkey=private_key)

    sftp = paramiko.SFTPClient.from_transport(transport)

    if style == 'put':
        sftp.put(local_file, remote_file)  # 将123.py 上传至服务器 /tmp下并改名为test.py
    elif style == 'get':
        sftp.get(remote_file, local_file)  # 将remove_path 下载到本地 local_path

    transport.close()


def sftp_keyfile_get_file(ip,port,username,keyfile,remote_file,local_file):
    '''
    example --> scp username@ip:remote_file local_file
    '''
    try:
        sftp_pwd(ip,port,username,keyfile,remote_file,local_file,style = 'get')
    except Exception as msg:
        print msg
    print "get [ %s ] is ok!" % remote_file


def sftp_keyfile_put_file(ip,port,username,keyfile,local_file,remote_file):
    '''
    example --> scp local_file username@ip:remote_file
    '''
    try:
        sftp_pwd(ip,port,username,keyfile,remote_file,local_file,style = 'put')
    except Exception as msg:
        print msg
    print "put [ %s ] is ok!" % local_file


# dump bin_source
def sftp_pwd_dump_bin_source(ip,port,username,passwd):
    try:
        pwn_name = ssh_base_pwd(ip,port,username,passwd,cmd="ls")

        pwn_name = pwn_name.strip()

        
        remote_file = '/home/'+username+'/'+pwn_name

        local_file = pwn_name+'-orig'

        sftp_pwd(ip,port,username,passwd,remote_file,local_file,style = 'get')

        print "dump [ %s ] is ok!" % remote_file
    except  Exception as msg:
        print msg


def sftp_keyfile_dump_bin_source(ip,port,username,keyfile):
    try:
        pwn_name = ssh_base_keyfile(ip,port,username,keyfile,cmd="ls")

        pwn_name = pwn_name.strip()

        
        remote_file = '/home/'+username+'/'+pwn_name

        local_file = pwn_name+'-orig'

        sftp_keyfile(ip,port,username,keyfile,remote_file,local_file,style = 'get')

        print "dump [ %s ] is ok!" % remote_file
    except  Exception as msg:
        print msg

# sftpdump('192.168.43.252',22,'pwn','123')
# sftp_dump_bin_source('192.168.43.252',22,'pwn','123')
# sftp_get_file('192.168.43.252',22,'pwn','123','/home/pwn/flag.txt','flag.txt')
# sftp_put_file('192.168.43.252',22,'pwn','123','flag.txt','/home/pwn/flag')
# sshdump('192.168.43.252',22,'pwn','123')
