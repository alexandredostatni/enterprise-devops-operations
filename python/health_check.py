import requests
import sys
from datetime import datetime

SERVICES = [
    "http://localhost:5000/health",
    "http://localhost:5000/"
]

def check_service(url):

    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            print(f"[OK] {url}")

        else:
            print(f"[ERROR] {url}: {response.status_code}")
            return False

    except requests.RequestException as error:

        print(f"[ERROR] {url}: {error}")
        return False

    return True

def main():

    print("TechCorp Infrastructure Health Check")
    print(datetime.now())

    results = [
        check_service(service)
        for service in SERVICES
    ]

    if not all(results):
        sys.exit(1)

    print("All services operational")

if __name__ == "__main__":
    main()