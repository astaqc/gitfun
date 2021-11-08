import subprocess
from github import Github





def status():
    return subprocess.getoutput("git status")


def push_branch(m:str,b:str,**url:str) -> str:
    try:    
        cmd_remote = "git remote add origin {0}".format(url)
        cmd_branch = "git checkout {} ".format(b)
        cmd_message = 'git commit -m "{}"'.format(m)
        cmd_push = "git push origin {}".format(b)
        if(b=="master" and b=="main" or m=="initial commit"):
            subprocess.getoutput('git init')
            subprocess.getoutput("git add .")  
            subprocess.getoutput(cmd_remote)
            print(cmd_remote)
            subprocess.getoutput(cmd_branch)
            print(cmd_message)
            subprocess.getoutput(cmd_message)
            result = subprocess.getoutput(cmd_push)
            return  result
        else:
            subprocess.getoutput(cmd_branch)  
            print(cmd_branch)   
            subprocess.getoutput("git add -u")
            subprocess.getoutput(cmd_message)
            print(cmd_message)
            result = subprocess.getoutput(cmd_push) 
            return  result
    except Exception as ex:
        print(ex)



def remote():
    return subprocess.getoutput("git remote -v")