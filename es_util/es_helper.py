from es_util.elasticsearch_config import es

def create_index(env_name, document):
	idVal = es.index(index='dev_logs',doc_type=env_name,body=document)
