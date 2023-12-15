import os
from dotenv import load_dotenv
from datetime import datetime
import platform


# Load variables from .env file
load_dotenv()


PROG_DIR = ""
if platform.system() == "Windows":
    PROG_DIR = os.environ.get('WINDOWS_PROG_DIR')
elif platform.system() == "Linux":
    PROG_DIR = os.environ.get('UNIX_PROG_DIR')
elif platform.system() == "Darwin":
    PROG_DIR = os.environ.get('MAC_PROG_DIR')

print("PROG_DIR: ",PROG_DIR)

def set_file_content(file_path,content):
    with open(file_path, 'w') as f:
        f.write(content)
    return True

def get_file_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    return content

# Run every 1 minutes to make sure the progress is not stocked at "working"
# It will reset the progress to "free" if it is stocked at "working" for more than 3 minutes
# print("Checking progress...")
if __name__ == "__main__":
    progress = get_file_content(f"{PROG_DIR}/progress.txt")
    progress = progress.split(",")
    if progress[0] == "working":
        timestamp = datetime.timestamp(datetime.now())
        diff = timestamp - float(progress[1])
        # print(diff)
        min3 = 60 * 3
        if diff > min3:
            set_file_content(f"{PROG_DIR}/progress.txt",f"free,{timestamp}")