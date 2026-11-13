import platform
import psutil
import json
from datetime import datetime

def generate_report():

    report = {
        "timestamp": str(datetime.now()),
        "hostname": platform.node(),
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory_percent": psutil.virtual_memory().percent,
        "disk_percent": psutil.disk_usage("/").percent
    }

    return report

if __name__ == "__main__":

    report = generate_report()

    print(json.dumps(report, indent=4))

    with open("resource_report.json", "w") as file:
        json.dump(report, file, indent=4)