import subprocess

def remote(url:str) -> str:
    subprocess.run("git add remote origin",url)
    return "remote add"