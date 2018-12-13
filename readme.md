# AutoBinForAWD

## 前言
开发这套工具的初衷是为了在线下AWD中能对二进制自动化的运维，此套工具也仅仅适用于传统CTF-AWD比赛中。
此套工具主文件有两个一个是命令行模式的`ssh`自动化连接工具，另一个是pwn题的批量自动化提交工具。

### 0x1 AutoBinary

```
usage: AutoBinary.py [-h] [--dump] [--find] [--get] [--put] [-c COMMAND]
                     [-ip HOSTNAME] [-P PORT] [-u USERNAME] [-p PASSWD]
                     [-k KEYFILE] [-r REMOTEPATH] [-l LOCALPATH] [-v]

optional arguments:
  -h, --help            show this help message and exit
  --dump                To dump binary source
  --find                To get the pathslist of flag
  --get                 To dump choose file from remote host,but if you want
                        get without losting privilege you prefect using [scp
                        -P user@hostname:remote_file local_file] to get file
  --put                 To put choose file to remote host，but if you want
                        put without losting privilege you prefect using [scp
                        -P port local_file user@hostname:remote_file] to put
                        file
  -c COMMAND, --command COMMAND
                        To exec command by ssh
  -ip HOSTNAME, --hostname HOSTNAME
                        Input remote hostname[ip]
  -P PORT, --port PORT  Input remote ssh or sftp port
  -u USERNAME, --username USERNAME
                        Input remote ssh username
  -p PASSWD, --passwd PASSWD
                        Input remote ssh passwd
  -k KEYFILE, --keyfile KEYFILE
                        Input ssh key file
  -r REMOTEPATH, --remotepath REMOTEPATH
                        Input remotepath file name to dump or overwrite it
  -l LOCALPATH, --localpath LOCALPATH
                        Input localpath file name
  -v, --version         Edit by BadRer V1.0
```


主要功能参数：

--dump      一键`dump` pwn题的源文件，用于`dump`用户工作目录下的单个源文件

--find      一键获取服务器上的`flag`所在的路径

--get       从远程服务器上获取文件 类似`scp -P port user@ip:remote_file local_file`

--put       上传文件到远程服务器上 类似`scp -P port local_file user@ip:remote_file` ,经过测试发现文件权限会发生变化，因此还是推荐使用`scp`

--command   通过`ssh`执行一些简单的命令，最常用的就是列目录

常用的命令：

python AutoBinary.py -ip 192.168.43.252 -P 22 -u pwn -p 123 --dump
python AutoBinary.py -ip 192.168.43.252 -P 22 -u pwn -p 123 --find
python AutoBinary.py -ip 192.168.43.252 -P 22 -u pwn -p 123 --command 'ls'
python AutoBinary.py -ip 192.168.43.252 -P 22 -u pwn -p 123 --get -r '/home/pwn/pwn1' -l pwn1
python AutoBinary.py -ip 192.168.43.252 -P 22 -u pwn -p 123 --put -l pwn1 -r '/home/pwn/pwn1'


### 测试

经过测试通过用户名密码登录的方式脚本可以成功运行
通过用户名和私钥登录的方式还有待测试。

### 0x2 batch_submit

批量自动化提交工具，拿到`exp`便可以打遍全场

#### 使用说明：

1. 首先完善`autoUtil/auto_submit.py`中的`submit_flag`函数实现自动交`flag`
2. 完善`autoUtil/auto_getflag.py`中的 `auto_get_submit` 函数 实现自动`cat flag` 并且提交，此时需要使用有效的`exp`
3. 运行 `batch_submit.py` 修改对应的`iplist`和`port`，以及采用何种批量方式


#### 批量化实现思路：


##### 多线程

利用`threading`模块，对于两个主机的批量测试通过，针对大量线程不知运行效果如何。

##### 多进程

利用`multiprocessing`模块，测试没通过，也就放弃了。

####

手动多进程，通过脚本模版，对每一个`ip`生成一个攻击脚本（在`submit`目录下），最后需要手动运行每个`sh`脚本，主要需要在`AutoBinForAWD`目录下，否则模块会导入错误
`submit`目录结构如下：
```
ip
    ip.py       具体的攻击脚本
    ip.sh       定时轮询的bash
    log.txt     输出日志

```

此方法在`PCB-Final`中使用并且针对此次比赛进行的优化

# 文尾

此套工具尚未成熟，不知在实战环境下效果如何，欢迎大家提`issues`


