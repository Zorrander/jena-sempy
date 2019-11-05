import requests

class Store:

    def __init__(self, address='127.0.0.1', dataset='Panda'):
        self.address = 'http://' + address + ':3030'
        self.dataset = dataset


    def select_all(self):
        request = """
        SELECT ?subject ?predicate ?object
        WHERE {
            ?subject ?predicate ?object
        }
        LIMIT 25
        """
        response = requests.post("{}/{}/query".format(self.address, self.dataset), data={'query': request})
        return response.json()

    def __str__(self):
        pass
