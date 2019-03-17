import requests

'''
Test for auto-submit-flag ! Try and complete it ！

example one :

def submit_flag(flag, token):
    url = "http://172.16.200.20:9000/submit_flag/"
    failed = ''
    data = {
        "flag":flag,
        "token":token
    }
    print "[+] Submiting flag : [%s]" % (data)
    response = requests.post(url, data=data)
    content = response.content
    print "[+] Content : %s" % (content)
    if failed in content:
        print "[-] failed!"
        return False
    else:
        print "[+] Success!"
        return True

example two :

def submitflag(flag):
    data = {}
    data['flag']= flag

    cookies = {}
    cookies['JSESSIONID']='967109F90DB4181BC03A7F19F631B21F'
    url = "http://172.91.1.12:9090/ad/hacker/submit/submitCode"
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0','Accept':'application/json, text/javascript, */*; q=0.01','Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2','Referer':'http://172.91.1.12:9090/arace/index','X-Requested-With':'XMLHttpRequest'}
    try:
        req = requests.post(url,data = data,cookies = cookies,headers = headers)
        print req.text
    except:
        print 'error'

'''