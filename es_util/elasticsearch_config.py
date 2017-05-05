from elasticsearch import Elasticsearch

# you can use RFC-1738 to specify the url
es = Elasticsearch(['http://elastic:changeme@localhost:9200'])
