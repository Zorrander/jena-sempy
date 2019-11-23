"""
Define a set of queries to retrieve information from an RDF Triple store.
"""


def add_limit(query, limit=25):
    return " LIMIT " + str(limit)

''' Select every triple in the store '''
def select_all():
    query = """
    SELECT ?subject ?predicate ?object
    WHERE {
        ?subject ?predicate ?object
    }
    """
    #query += add_limit(query)
    return query

def select_skill(action, target):
    query = """
        SELECT ?skill
        WHERE {
            ?entity rdfs:subClassOf      cogtuni:Utterance ;
                    cogtuni:isInvokedBy  ?sl1;
                    cogtuni:isFollowedBy ?sl2;
                    cogtuni:activates    ?skill.
            ?sl1 cogtuni:hasValue """+ "'" + action + "'" + """.
            ?sl2 cogtuni:hasValue """ + "'" + target + "'" + """.
        }
        """
    return query
