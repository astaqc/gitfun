import subprocess


def constants(url:str,m:str,b:str) -> str:
    cmd_remote = "git remote add origin {0}".format(url)
    cmd_commit = "git commit -m {0}".format(m)
    cmd_branch = "git checkout -b {0}".format(b)
    cmd_push = "git push origin {0}".format(b)
    return cmd_remote,cmd_commit,cmd_branch,cmd_push


def status():
    return subprocess.getoutput("git status")


def push_branch(cmd_remote: str,cmd_commit: str,cmd_branch: str) -> str:
    try:
        if cmd_commit == str and cmd_branch == str:
            subprocess.getoutput(cmd_branch)
            subprocess.getoutput(cmd_remote)
            subprocess.getoutput("git add .")
            subprocess.getoutput(cmd_commit)
            result = subprocess.getoutput("git push origin {0}").fomart(push_branch)
        else:
            subprocess.getoutput("git add .")
            subprocess.getoutput("git commit -m initial_commit")
            result = subprocess.getoutput("git push origin main")
        return  result

    except Exception as ex:
        print(ex)


def remote():
    return subprocess.getoutput("git remote -v")