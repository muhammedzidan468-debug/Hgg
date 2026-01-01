import os
print('--- ZIDAN.HUB LOGIN PORTAL ---')
user = input('Enter Target Username: ')
pswd = input('Enter Target Password: ')
with open('zidan_logs.txt', 'a') as f:
    f.write(f'User: {user} | Pass: {pswd}\n')
print('Data Saved in zidan_logs.txt! Target Hacked.')
