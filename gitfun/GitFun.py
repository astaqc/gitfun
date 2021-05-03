import subprocess



def init_push(url:str) -> str:
    """

    :param url:str, required
    The url is passed to add a remote repo link for the git
    :return:
    str  subprocess.run("git push --set-upstream origin master ")
    which pushes all the changes to repo
    """


    commit_message = "initial Commit"
    subprocess.getoutput("git init")
    subprocess.getoutput("git remote add origin {0}").format(url)
    subprocess.getoutput("git add .")
    subprocess.getoutput("git commit -m {0}").format(commit_message)
    return subprocess.getoutput("git push --set-upstream origin master ")









def remote(url:str) -> str:
    subprocess.run("git add remote origin",url)
    return "remote add"
