import requests

username = "ruhan_kazmi_1122"
print(f"Checking status for: {username}")

# Instagram server request test
response = requests.get(f"https://www.instagram.com/{username}/")
if response.status_code == 200:
    print("Account Active: Abhi ban nahi hua.")
else:
    print(f"Status: {response.status_code}. Shayad block ho raha hai.")

