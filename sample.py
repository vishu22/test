import os
from pyes import *

es_port = 9200
conn = ES('http://127.0.0.1:{0}'.format(es_port)) # Use HTTP
try:
    conn.indices.delete_index("test-index")
except:
    pass

conn.indices.create_index("test-index")

mapping = {
    'parsedtext': {
        'boost': 1.0,
        'index': 'analyzed',
        'store': 'yes',
        'type': 'string',
        "term_vector": "with_positions_offsets"
    },
    'name': {
        'boost': 1.0,
        'index': 'analyzed',
        'store': 'yes',
        'type': 'string',
        "term_vector": "with_positions_offsets"
    },
    'title': {
        'boost': 1.0,
        'index': 'analyzed',
        'store': 'yes',
        'type': 'string',
        "term_vector": "with_positions_offsets"
    },
    'pos': {
        'store': 'yes',
        'type': 'integer'
    },
    'uuid': {
        'boost': 1.0,
        'index': 'not_analyzed',
        'store': 'yes',
        'type': 'string'
    }
}
conn.indices.put_mapping("test-type", {'properties':mapping}, ["test-index"])

conn.index({"name":"Joe Tester", "parsedtext":"Joe Testere nice guy", "uuid":"11111", "position":1}, "test-index", "test-type", 1)
conn.index({"name":"Bill Baloney", "parsedtext":"Joe Testere nice guy", "uuid":"22222", "position":2}, "test-index", "test-type", 2)

conn.indices.refresh("test-index") # Single index.

q = TermQuery("name", "joe")
results = conn.search(query = q)

for r in results:
   print r
