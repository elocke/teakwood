from rq import Queue
from redis import Redis
# from processMetadata import ImportShow
import time
import processMetadata_v3
from internetarchive import search_items

search = search_items('mediatype:etree AND creator:"Blue Turtle Seduction"')


redis_conn = Redis('redis')
q = Queue(connection=redis_conn)

for result in search:
	print result['identifier']
	job = q.enqueue(processMetadata_v3.main, result['identifier'])
	