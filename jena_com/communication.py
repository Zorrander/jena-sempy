import requests

class Server:

    def __init__(self, ip='127.0.0.1', port='3030' dataset='Panda'):
        self.address = 'http://' + ip + ':' + port
        self.dataset = dataset


    def send(self, query):
        response = requests.post("{}/{}/query".format(self.address, self.dataset), data={'query': query})
        return response.json()
