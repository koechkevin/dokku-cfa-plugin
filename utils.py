#!/usr/bin/env python3

import subprocess

def pip_install(dependancy):
    try:
        subprocess.check_call(["pip", "install", dependancy])
    except subprocess.CalledProcessError:
         print("Failed to install '{dependancy}'")