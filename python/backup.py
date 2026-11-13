import os
import shutil
from datetime import datetime

SOURCE = "application"
BACKUP_DIR = "backups"

def create_backup():

    os.makedirs(BACKUP_DIR, exist_ok=True)

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    destination = os.path.join(
        BACKUP_DIR,
        f"backup_{timestamp}"
    )

    shutil.copytree(
        SOURCE,
        destination,
        ignore=shutil.ignore_patterns(
            "venv",
            "__pycache__"
        )
    )

    print(f"Backup created: {destination}")

if __name__ == "__main__":
    create_backup()