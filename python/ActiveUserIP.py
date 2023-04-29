#!/usr/bin/env python3
import subprocess

def get_active_user_ip():
    cmd = "who -u -m | awk '{print $NF}' | sed -e 's/[()]//g'"
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    output, _ = process.communicate()
    
    #unmodified output usually returns "b'<IP ADDRESS>'"
    return output.strip().decode().replace('b', '').replace('\'', '')

if __name__ == "__main__":
    print(get_active_user_ip())
