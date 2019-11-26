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

def select_steps(skill_name):
    query = """
        SELECT ?s
        WHERE {
        cogrobtut:""" + skill_name + """ cogrobtut:hasStep ?step .
        bind( strafter(str(?step), "#") as ?s) . }
    """
    return query

def select_previous_state_and_first_task(step_name):
    query = """
        SELECT ?o ?previousState
        WHERE {
        cogrobtut:""" + step_name + """ cogrobtut:consistsIn ?val .
        OPTIONAL{cogrobtut:""" + step_name + """ cogrobtut:isDoneAfter ?ps. }
        bind( strafter(str(?ps), "#") as ?previousState)
        bind( strafter(str(?val), "#") as ?o) .
        }
    """
    return query

def select_next_task(previous):
    query = """
        SELECT ?second
        WHERE {
        OPTIONAL{cogrobtut:""" + previous + """ cogrobtut:doesThen ?o2. }
        BIND( strafter(str(?o2), "#") as ?second) .
        }
    """
    return query
