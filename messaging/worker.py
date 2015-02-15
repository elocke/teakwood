# -*- coding: utf-8 -*-
# from processMetadata import ImportShow
from redis import Redis
from rq import Connection, Queue, Worker


if __name__ == '__main__':
    # Tell rq what Redis connection to use
    with Connection(Redis(host='redis')):
        q = Queue()
        Worker(q).work()
