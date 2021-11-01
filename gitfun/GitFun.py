import subprocess


def constants(url:str,m:str,b:str) -> str:
    cmd_remote = "git remote add origin {0}".format(url)
    cmd_commit = "git commit -m {0}".format(m)
    cmd_branch = "git checkout -b {0}".format(b)
    cmd_push = "git push origin {0}".format(b)
    return cmd_remote,cmd_commit,cmd_branch,cmd_push


def status():
    return subprocess.getoutput("git status")


def push_branch(url,m,b) -> str:
    try:    
        if(b=="master" or b=="main" or  m=="initial commit"):
            subprocess.getoutput('git checkout {0} ').format(b)      
            subprocess.getoutput('git init')
            subprocess.getoutput("git add .")
            subprocess.getoutput("git commit -m {0}").format(m)
            result = subprocess.getoutput("git push origin {0}").format(b)
            return  result
        else:
            subprocess.getoutput('git checkout {0} ').format(b)      
            subprocess.getoutput('git init')
            subprocess.getoutput("git add .")
            subprocess.getoutput("git commit -m {0}").format(m)
            result = subprocess.getoutput("git push origin {0}").format(b)
            return  result


    except ValueError as ex:
        print(ex)


def remote():
    return subprocess.getoutput("git remote -v")