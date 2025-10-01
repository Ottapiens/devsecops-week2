def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Tidak boleh bagi nol")
    return a / b

import subprocess

def run_command(cmd):
    # Fixed: No shell=True, use list for args
    result = subprocess.run(cmd.split(), capture_output=True, text=True)  # Asumsi cmd string aman
    return result.stdout