import requests


class Dreadnot(object):
    def __init__(self, baseUrl, auth=None):
        self._baseUrl = baseUrl
        self._auth = auth

    def _url(self, paths):
        return self._baseUrl + '/api/1.0/' + '/'.join(paths)

    def get(self, paths, *args, **kwargs):
        return requests.get(self._url(paths), *args, auth=self._auth, **kwargs)

    def post(self, paths, params, *args, **kwargs):
        return requests.post(self._url(paths), *args, auth=self._auth, params=params, **kwargs)

    def deploy(self, stack, region, to_revision):
        return self.post(['stacks', stack, 'regions', region, 'deployments'], {'to_revision': to_revision}).json

    def deployment(self, stack, region, deploy_name):
        return self.get(['stacks', stack, 'regions', region, 'deployments', deploy_name]).json

    def deployments(self, stack, region):
        return self.get(['stacks', stack, 'regions', region, 'deployments']).json

    def stacks(self):
        return self.get(['stacks']).json

    def regions(self, stack):
        return self.get(['stacks', stack, 'regions']).json
