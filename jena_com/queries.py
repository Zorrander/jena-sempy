"""
Define a set of queries to retrieve information from an RDF Triple store.
"""


def add_limit(self, query, limit=25):
    return " LIMIT " + limit

''' Select every triple in the store '''
def select_all(self):
    query = """
    SELECT ?subject ?predicate ?object
    WHERE {
        ?subject ?predicate ?object
    }
    """
    query += add_limit(query)
    return query
