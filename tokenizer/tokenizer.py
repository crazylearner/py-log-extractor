
from collections import namedtuple
import json

LogData = namedtuple('LogData','emitted_at priority_syslog_version host_name app_name proc_id msg_id log_level log_message')

def process_extract_log(logstring, appname):
	all_logs = logstring.split('\n')
	logs = []
	print('length')
	print(len(all_logs))
	for log in all_logs:
		logs.append(extract_log_data(log, appname))
	return logs

def extract_log_data(logdata, appname):
	"""Tokenizes each log string, that comes from heroku.
	Assumed that the log lokks like this: 
	242 <190>1 2017-04-25T10:00:49.725783+00:00 host app web.1 - 2017-04-25 10:00:49 [index:api] INFO  [http-nio-12057-exec-8] [tId:] [rId:] 		[tt:] GSAL:method=GET path='/api/v1.0/tenants/provision' pattern='' query='null' user='' role='' status=405"
	heroku metadata[type of log, priority, timestamp, host, app info] - actual log from application
	"""
	split_log = logdata.split(' - ')
	print(split_log)
	if( len(split_log) < 2 ) :
		#throw error
		return {};
	metadata = split_log[0]

	metadata_arr = metadata.split(' ')
	print(metadata_arr)
	if(len(metadata_arr) != 6):
		#throw error
		return {}
	priority_syslog = metadata_arr[1]
	emitted_at = metadata_arr[2]
	host_name = metadata_arr[4]
	proc_id = metadata_arr[5]

	if('logplex' == proc_id):
		#process differently. (More than one logs are present based on info at split_log[2] .. has to be processed differently.)
		actual_log = split_log[len(split_log) - 1]
	else:
		actual_log = split_log[1]

	
	log_level = get_log_level(actual_log)
	log_data = LogData(emitted_at, priority_syslog, host_name, appname, proc_id, '', log_level, actual_log)
	return json.dumps(log_data._asdict())

def get_log_level(log):
	if('WARN' in log):
		return 'WARN'
	elif('ERROR' in log):
		return 'ERROR'
	elif('INFO' in log):
		return 'INFO'
	elif('DEBUG' in log):
		return 'DEBUG'
