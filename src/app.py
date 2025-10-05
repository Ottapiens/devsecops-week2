import subprocess
import shlex  # Untuk memecah cmd dengan aman

def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Tidak boleh bagi nol")
    return a / b

def run_command(cmd):
    # Gunakan shlex.split() untuk memisahkan argumen dengan aman
    # dan hilangkan shell=True agar tidak lewat shell interpreter
    if isinstance(cmd, str):
        cmd = shlex.split(cmd)
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Command failed: {e.stderr}"