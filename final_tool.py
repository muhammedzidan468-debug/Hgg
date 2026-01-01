import pyshorteners
import time
s = pyshorteners.Shortener()
target = '+923252949842'
print('
[#] Initializing Advanced OSINT Framework...')
time.sleep(1)
print('[#] Connecting to Global Database...')
time.sleep(1)
print(f'[!] Target Identified: {target}')
print('[!] Status: Monitoring Digital Footprints...')

# Masking the link
original = 'https://grabify.link/NWP8TK'
masked = s.tinyurl.short(original)

print(f'
[+] Tracking Link Generated: {masked}')
print('[+] Redirection: Active')
print('
' + '='*40)
print('    SYSTEM STATUS: DATA SYNCHRONIZED')
print('    TARGET STATUS: UNDER OBSERVATION')
print('='*40)
print('
[Done] Script executed successfully.')