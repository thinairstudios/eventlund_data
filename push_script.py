from git import Repo

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

