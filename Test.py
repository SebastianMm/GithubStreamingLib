import requests
import json

class GitHub():

    def __init__(self, owner, repo, resources):
        self.owner = owner
        self.repo = repo
        self.resources = resources
        
    def read(self):
        params = {'page': 0, 'per_page':25}
        another_page = True
        while another_page:
                for rep in self.repo:
                    for res in self.resources:
                        url = 'https://api.github.com/repos/{}/{}/{}'.format(self.owner, rep, res)
                        result = requests.get(url,params=params) #can also add headers = {"Authorization": git_token} for more requests per IP
                        if result.status_code == 200:      
                                if 'next' in result.links:
                                        yield {'url': url, 'result': result.json(), 'page':result.links['next']['url']}                
                                else:
                                        another_page = False
                        else:
                                raise ValueError('API rate limit exceeded for {}.'.format(self.get_ip))
                                
gh = GitHub('moby', ['moby', 'buildkit'], ['issues','pulls'])
data = gh.read()
while data is not None:
    for result in data:
        print('url: {}\tlen(result): {}\t page: {}'.format(result['url'], len(result['result']), result.links['next']['url']))
