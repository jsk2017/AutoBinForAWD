from auto_ssh import *


def ssh_dump(ip,port,username,passwd,keyfile):
    if passwd:
        sftp_pwd_dump_bin_source(ip,port,username,passwd)
    elif keyfile:
        sftp_keyfile_dump_bin_source(ip,port,username,keyfile)


def ssh_find(ip,port,username,passwd,keyfile):
    if passwd:
        ssh_pwd_get_flag_path(ip,port,username,passwd)
    elif keyfile:
        ssh_base_keyfile_get_flag_path(ip,port,username,keyfile)


def ssh_get(ip,port,username,passwd,keyfile,remotepath,localpath):
    if passwd:
        sftp_pwd(ip,port,username,passwd,remotepath,localpath,style='get')
    elif keyfile:
        sftp_keyfile(ip,port,username,keyfile,remotepath,localpath,style='get')


def ssh_put(ip,port,username,passwd,keyfile,localpath,remotepath):
    if passwd:
        sftp_pwd(ip,port,username,passwd,remotepath,localpath,style='put')
    elif keyfile:
        sftp_keyfile(ip,port,username,keyfile,remotepath,localpath,style='put')


def ssh_exec(ip,port,username,passwd,keyfile,command):
    if passwd:
        ssh_pwd_print_result(ip,port,username,passwd,cmd=command)
    elif keyfile:
        ssh_base_keyfile_print_result(ip,port,username,keyfile,cmd=command)


# ip = '192.168.43.252'
# port = 10000
# username = 'pwn'
# passwd = '123'

# ssh_base_pwd(ip,port,username,passwd,cmd='ls') 
# ssh_pwd_print_result(ip,port,username,passwd,cmd='ls')
# ssh_pwd_get_flag_path(ip,port,username,passwd)

# sftp_pwd(ip,port,username,passwd,remote_file,local_file,style)
# sftp_pwd_dump_bin_source("192.168.43.252",22,'pwn','123')


'''
ssh_base_keyfile(ip,port,username,keyfile,cmd='ls')
ssh_base_keyfile_print_result(ip,port,username,keyfile,cmd='ls')
ssh_base_keyfile_get_flag_path(ip,port,username,keyfile,cmd='ls')

sftp_keyfile(ip,port,username,keyfile,remote_file,local_file,style)
sftp_keyfile_dump_bin_source(ip,port,username,keyfile)
'''

