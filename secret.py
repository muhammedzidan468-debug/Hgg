import time, sys
message = input('Apna secret message likho: ')
hacker_code = input('Hacker Code (e.g. 007): ')
print('\n[!] NASA Servers se connect ho raha hai...')
time.sleep(1)
print('[!!] SCOM ka data access kiya ja raha hai...')
time.sleep(1)
for i in range(21):
    sys.stdout.write(f'\rHacking NASA... [{"#" * i}{"." * (20-i)}] {i*5}%')
    sys.stdout.flush()
    time.sleep(0.1)
print(f'\n\n[SUCCESS] Zidan Bhai, aapka message: "{message}" NASA ki screen par chipak gaya!')
print(f'Hacker Code "{hacker_code}" activate ho gaya hai. Ab sab seedhe ho jayenge! 😎')
