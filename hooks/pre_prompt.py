import sys
import subprocess

def is_docker_installed() -> bool:
    try:
        subprocess.run(["docker", "--version"], capture_output=True, check=True)
        return True
    except Exception:
        return False

def is_poetry_installed() -> bool:
    try:
        subprocess.run(["poetry", "about"], capture_output=True, check=True)
        return True
    except Exception:
        return False

    
if __name__ == "__main__":
    if not is_docker_installed():
        print("ERROR: Docker is not installed.")
        sys.exit(1)
    if not is_poetry_installed():
        print("ERROR: Poetry is not installed.")
        sys.exit(1)