import requests
import urllib.request

class GitHub():

    def __init__(self, owner, repo, resources):
        self.owner = owner
        self.repo = repo
        self.resources = resources

    def get_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            # doesn't even have to be reachable
            s.connect(('10.255.255.255', 1))
            IP = s.getsockname()[0]
        except:
            IP = '127.0.0.1'
        finally:
            s.close()

    def read(self):
        for rep in self.repo:
            for res in self.resources:
                url = 'https://api.github.com/repos/{}/{}/{}'.format(self.owner, rep, res)
                result = requests.get(url)
                if result.status_code == 200:
                    yield {'url': url, 'result': result.json()}
                else:
                    raise ValueError('API rate limit exceeded for {}.'.format(self.get_ip))
                
    def getAvatar(self):
        url = 'https://api.github.com/users/{}'.format(self.owner)
        r = requests.get(url)
        j = json.loads(r.text)
        avatar = j['avatar_url']
        urllib.request.retrieve(avatar, "moby.jpg")
        
gh = GitHub('moby', ['moby', 'buildkit'], ['issues','pulls'])
data = gh.read()
while data is not None:
    for result in data:
        print('url: {}\tlen(result): {}'.format(result['url'], len(result['result'])))
gh.getAvatar()

