"""Executes shell commands with timeout."""
import subprocess
def run_cmd(cmd, timeout=30):
    return subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=timeout)
