import requests
import json

class NetworkReachabilityChecker:
    def __init__(self, device_ip):
        self.device_ip = device_ip

    def ping(self):
        try:
            response = requests.get(f'http://{self.device_ip}/ping')
            return response.status_code == 200
        except requests.exceptions.RequestException:
            return False

    def traceroute(self):
        try:
            response = requests.get(f'http://{self.device_ip}/traceroute')
            return response.status_code == 200
        except requests.exceptions.RequestException:
            return False

    def check_reachability(self):
        return self.ping() or self.traceroute()

def main():
    device_ip = input("Ishlatiladigan qurilma IP manzilini kiriting: ")
    checker = NetworkReachabilityChecker(device_ip)
    if checker.check_reachability():
        print("Qurilmaga ulanish mavjud.")
    else:
        print("Qurilma bilan ulanish mavjud emas.")

if __name__ == "__main__":
    main()
```

Kodda quyidagi funksiyalar mavjud:

- `ping()`: Qurilma bilan ulanishni tekshirish uchun ping so'rovini yuboradi.
- `traceroute()`: Qurilma bilan ulanishni tekshirish uchun traceroute so'rovini yuboradi.
- `check_reachability()`: `ping()` va `traceroute()` funksiyalarining bittasi ishlaydi yoki ikkalasi ham ishlaydi.
- `main()`: Foydalanuvchi tomonidan qurilma IP manzilini so'raydi va `NetworkReachabilityChecker` obyektini yaratadi. Keyin `check_reachability()` funksiyasini chaquradi va natijani chiqaradi.
