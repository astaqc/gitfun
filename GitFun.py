import subprocess



def init_push(url:str,m:str) -> str:
    """

    :param url:str, required
    The url is passed to add a remote repo link for the git
    :return:
    str  subprocess.run("git push --set-upstream origin master ")
    which pushes all the changes to repo
    """


    subprocess.getoutput("git init")
    subprocess.getoutput("git remote add origin {0}").format(url)
    subprocess.getoutput("git add .")
    try:
        if m == type(str):
            subprocess.getoutput("git commit -m {0}").format(m)
        else:
            subprocess.getoutput("git commit -m initial commit")
    except Exception as ex:
        print(ex)
    return subprocess.getoutput("git push --set-upstream origin master ")









def status():
    return subprocess.getoutput("git status")
