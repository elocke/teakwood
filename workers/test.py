import time
from internetarchive import search_items

search = search_items('mediatype:collection AND collection:etree', fields=['identifier','collection'])


for result in search:
	print result['identifier'], result['collection'][0]
	

from rq import Queue
from redis import Redis
# from processMetadata import ImportShow
import time
import processMetadata_v3
from internetarchive import search_items



# sstring = 'mediatype:etree AND creator:"Blue Turtle Seduction"'
sstring = 'mediatype:collection AND collection:etree'
search = search_items(sstring)


redis_conn = Redis('redis')
q = Queue(connection=redis_conn)

for result in search:
	print result['identifier']
	job = q.enqueue(processMetadata_v3.main, result['identifier'])
		