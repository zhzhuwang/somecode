import os
from pathlib import Path

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOG_DIR = os.path.join(BASE_DIR, "logs")
LOG_IMG = os.path.join(LOG_DIR, "log_img")
TEST_LOGS_PATH = os.path.join(LOG_DIR, "cases.log")

if Path(LOG_DIR).is_dir():
    pass
else:
    Path(LOG_DIR).mkdir()

if Path(LOG_IMG).is_dir():
    pass
else:
    Path(LOG_IMG).mkdir()
