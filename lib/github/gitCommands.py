import git 

class gitCMD:
    def __init__(self, directory):
        self.repo = git.Repo(directory)
        self.git = self.repo.git

    def pull(self):
        self.git.pull()

    def push(self):
        self.git.push()

    def add(self, file):
        self.git.add(file)
    
if __name__ == "__main__":
    gitCMD = gitCMD(".")
    gitCMD.pull()
    gitCMD.push()
    gitCMD.add("README.md")