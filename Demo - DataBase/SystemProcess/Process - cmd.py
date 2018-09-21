import subprocess
import os

print("$ nslookup www.python.org")

# 执行cmd命令 此方法为阻塞的
result = subprocess.call("notepad")
result = subprocess.call("mstsc")

os.system("notepad")

print("Exit code:", result)吧