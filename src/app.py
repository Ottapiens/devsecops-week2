import subprocess  # nosec B404
import shlex

def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Tidak boleh bagi nol")
    return a / b

def run_command(cmd: str):
    """
    Jalankan perintah dengan aman.
    - shell=False (mencegah command injection)
    - Hanya jalankan perintah yang diizinkan (whitelist)
    """
    allowed_cmds = {
        "date": ["date"],
        "whoami": ["whoami"],
        "uptime": ["uptime"]
    }

    if cmd not in allowed_cmds:
        return "Perintah tidak diizinkan."

    try:
        result = subprocess.run(  # nosec B603
            allowed_cmds[cmd],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr.strip()}"


