from rq import Queue
from redis import Redis
# from processMetadata import ImportShow
import time
import processMetadata_v3
from internetarchive import search_items

def queueSearch(search_string):
	redis_conn = Redis('redis')
	q = Queue(connection=redis_conn)
	search = search_items(search_string)

	for result in search:
		print result['identifier']
		job = q.enqueue(processMetadata_v3.main, result['identifier'])




# Small Samples
queueSearch('mediatype:etree AND (creator:Spafford OR creator:"Perpetual Groove" OR creator:Zoogma OR creator:"Mountain Standard Time")')

queueSearch('mediatype:etree AND (creator:Lotus OR creator:"New Monsoon")')


# Full Artist Load
# queueSearch('mediatype:collection AND collection:etree')
# Full Show Load
# queueSearch('mediatype:etree')
