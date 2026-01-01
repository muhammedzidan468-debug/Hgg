import os
import time

print("--- GHOST MODE ACTIVATED (FBI STYLE) ---")
print("Zidan Bhai, ab aapka saaya bhi aapko nahi dhoond payega...")

while True:
    os.system("cd ~/nipe && perl nipe.pl restart")
    print("\n[+] IP Changed Successfully!")
    os.system("curl -s ipinfo.io/ip")
    os.system("curl -s ipinfo.io/country")
    print("-" * 30)
    time.sleep(10) # 10 second ka maza
