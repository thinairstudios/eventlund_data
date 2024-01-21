from git import Repo

PATH_OF_GIT_REPO = r'/.git'  # make sure .git folder is properly configured
COMMIT_MESSAGE = 'comment from python script'

def git_push():
    try:
        repo = Repo('/home/ubuntu/eventlund_data/.git')
        repo.git.add('push_script.py')
        repo.index.commit('auto update')
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print('Some error occured while pushing the code')    

git_push()

