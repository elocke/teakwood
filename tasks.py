from rq import Queue
from redis import Redis
# from processMetadata import ImportShow
import time
import processMetadata_v2

redis_conn = Redis('redis')
q = Queue(connection=redis_conn)

job = q.enqueue(processMetadata_v2.processQuick, 'tlg2006-10-21.mk4v.flac16')
print job.result
print q.jobs
time.sleep(2)
print job.result

time.sleep(2)
print job.result
