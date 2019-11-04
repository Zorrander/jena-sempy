import requests

class Store:

    def __init__(self, address='127.0.0.1', dataset='Panda'):
        self.address = 'http://' + address + ':3030'
        self.dataset = dataset


    def request(self):
        request = """
        SELECT ?subject ?predicate ?object
        WHERE {
            ?subject ?predicate ?object
        }
        LIMIT 25
        """
        print("Sending request to: {}/{}/query".format(self.address, self.dataset))
        print("request = {}".format(request))
        response = requests.post("{}/{}/query".format(self.address, self.dataset), data={'query': request})
        return response.json()

    def __str__(self):
        pass
