import phonenumbers
from phonenumbers import geocoder, carrier

def advanced_osint(number):
    try:
        parsed = phonenumbers.parse(number)
        location = geocoder.description_for_number(parsed, "en")
        service = carrier.name_for_number(parsed, "en")
        
        print(f"\n[+] Information for: {number}")
        print(f"[-] Location: {location}")
        print(f"[-] Carrier: {service}")
        
        # Social Media Search Links
        print("\n[!] Scanning Digital Footprints...")
        clean_number = number.replace("+", "")
        
        print(f"--> WhatsApp: https://wa.me/{clean_number}")
        print(f"--> Facebook Search: https://www.facebook.com/search/top/?q={clean_number}")
        print(f"--> Google Search: https://www.google.com/search?q=%22{number}%22")
        
    except Exception as e:
        print(f"Error: {e}")

target = "+923252949842"
advanced_osint(target)

