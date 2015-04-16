# from app.models import *
import json
import os
# import argparse
from datetime import datetime
from operator import itemgetter
import requests
# import pprint
# from internetarchive import get_item
import unirest
# from mongoengine import connect
# from models import *
import sys
import arrow
import time 
# connect('teakwood', host='db', port=27017)
ENTRY_POINT = 'http://192.168.1.4:8080/api'



# def getMeta(archiveid):
#     url = 'http://archive.org/metadata/{identifier}'.format(identifier=archiveid)
#     try:
#         resp = requests.get(url)
#         resp.raise_for_status()
#     except HTTPError as e:
#         error_msg = 'Error retrieving metadata from {0}, {1}'.format(resp.url, e)
#         log.error(error_msg)
#         raise HTTPError(error_msg)
#     metadata = resp.json()
#     return metadata

def getMeta(identifier):
    url = 'http://archive.org/metadata/{identifier}'.format(identifier=identifier) 
    thread = unirest.get(url)
    return thread.body


def endpoint(resource):
    return '%s/%s/' % (ENTRY_POINT, resource)

def readResponse(response):
    # print response
    response.code # The HTTP status code
    response.headers # The HTTP headers
    response.body # The parsed response
    response.raw_body # The unparsed response

    # check here for success or fail 
    # handle exceptions here

    # valids = []
    # if r.status_code == 201:
    #     response = r.json()
    #     if response['_status'] == 'OK':
    #         for artist in response['_items']:
    #             if artist['_status'] == "OK":
    #                 valids.append(artist['_id'])

    # return valids    
    return response.body

def perform_post(resource, data):
    headers = {'Content-Type': 'application/json'}
    thread = unirest.post(endpoint(resource), headers=headers, params=json.dumps(data))
    # print thread.code, thread.headers, thread.raw_body
    if thread.code in (422, 404):
        print 'ERROR in POST of %s' % data['identifier']
        print 'RESPONSE %s' % thread.raw_body
        raise Exception
    return thread

def postArtist(artist):
    # print artist
    # print json.dumps(artist)
    try:    
        r = perform_post('artists', artist)
        print "artist %s posted, STATUS: %s" % (artist['name'], r.code)
        return r
    except Exception, e:
        print e
        print 'ERROR posting artist:  %s' % artist['name']
        

def postShow(show):
    # print show
    # print json.dumps(show)
    try:
        r = perform_post('shows', show)
        print "show %s posted, STATUS: %s" % (show['identifier'], r.code)
        return r
    except Exception, e:
        print e
        print 'ERROR posting show:  %s' % show['identifier']
        # print 'RESPONSE %s' % r.raw_body        

def getArtistId(identifier):
    url = endpoint('artists') + identifier
    # print url
    thread = unirest.get(url)
    if thread.code == 404:
        # raise('Error getting artist id')
        return False
        # sys.exit()
    else:
        return thread.body['_id']

def processCollection(metadata):
    artist_dict = {}
    meta = metadata['metadata']
    artist_dict['name'] = meta['creator']
    artist_dict['identifier'] = meta['identifier']
    if 'rights' in meta: artist_dict['rights'] = meta['rights']
    artist_dict['addeddate'] = parseDate(meta['addeddate'])
    # artist_dict['years'] = []
    # artist_dict['show_count'] = 0
    # print artist_dict['addeddate']
    # artist_dict['addeddate'] = meta['addeddate']
    return artist_dict


def parseDate(dateobj):
    output_format = "YYYY-MM-DD HH:mm:ss"
    # output_format = "ddd, d MMM YYYY HH:mm:ss"
    if isinstance(dateobj, list):
        # print arrow.get(dateobj[-1]).format(output_format)
        # result = str(datetime.strptime(dateobj[-1], "%Y-%m-%d %H:%M:%S").strftime(output_format)) # xxxx-xx-xx xx:xx:xx
        result = arrow.get(dateobj[-1]).format(output_format)
    else:
        # print arrow.get(dateobj).format(output_format)        
        # result = str(datetime.strptime(dateobj, "%Y-%m-%d %H:%M:%S").strftime(output_format)) # xxxx-xx-xx xx:xx:xx
        result = arrow.get(dateobj).format(output_format)
    return result


def processShow(metadata):
    print datetime.now()

    if 'metadata' in metadata:
        meta = metadata['metadata']
    else:
        raise('No metadata to process')

    if 'files' in metadata: files = metadata['files']
    if 'reviews' in metadata: reviews = metadata['reviews']
    show_dict = {}


    show_dict['identifier'] = meta['identifier']
    show_dict['artist_identifier'] = meta['collection'][0]

    if 'creator' in meta:
        if isinstance(meta['creator'], list):
            show_dict['creator'] = meta['creator'][0]
        else:
            show_dict['creator'] = meta['creator']

    show_dict['title'] = meta['title']
    if 'coverage' in meta: show_dict['location'] = meta['coverage']
    if 'venue' in meta: show_dict['venue'] = meta['venue']
    # if 'year' in meta: show_dict['year'] = meta['year']

    if 'date' in meta: show_dict['date'] = parseDate(meta['date'])
    if 'addeddate' in meta: show_dict['addeddate'] = parseDate(meta['addeddate'])        
    if 'updatedate' in meta: show_dict['updatedate'] = parseDate(meta['updatedate'])        

    if 'description' in meta: show_dict['description'] = meta['description']

    # Recording Info
    if 'taper' in meta: show_dict['taper'] = meta['taper']
    if 'transferer' in meta: show_dict['transferer'] = meta['transferer']
    if 'uploader' in meta: show_dict['uploader'] = meta['uploader']
    if 'lineage' in meta: show_dict['lineage'] = meta['lineage']
    if 'source' in meta: show_dict['source'] = meta['source']

    # Files, append only MP3
    if 'files' in metadata: 
        show_dict['files'] = []
        temp_list = []
        for f in files:
            tempd = {}
            if 'MP3' in f['format']:
                if str(f['format']).upper() == 'VBR MP3' :
                    tempd['mp3_bit'] = 1
                    tempd['mp3_hq_bit'] = 1
                if str(f['format']).upper() == '64KBPS MP3':
                    tempd['mp3_bit'] = 1   
                    tempd['mp3_hq_bit'] = 0
                     
                tempd['file_name'] = f['name']
                tempd['file_format'] = f['format']
                if 'title' in f: tempd['title'] = f['title']
                if 'track' in f: tempd['track'] = f['track']
                else:
                    # TODO: regex match d1tXX.mp3
                    pass
                if 'length' in f: tempd['length'] = f['length']  # convert to ms
                if 'bitrate' in f: tempd['bitrate'] = f['bitrate']
                temp_list.append(tempd)

        newlist = sorted(temp_list, key=itemgetter('file_name'))
        show_dict['files'] = newlist

    if 'reviews' in metadata:
        show_dict['comments'] = []
        for review in reviews:
            tempd = {}
            tempd['date'] = parseDate(review['createdate'])
            tempd['title'] = review['reviewtitle']
            tempd['content'] = review['reviewbody']
            tempd['reviewer'] = review['reviewer']
            tempd['rating'] = review['stars']
            show_dict['comments'].append(tempd)

    return show_dict


def main(archiveid):
    metadata = getMeta(archiveid)
    if 'is_collection' in metadata:
        # process as artist
        artist = processCollection(metadata)
        postArtist(artist)
        # raise Exception('is a collection')
    else:
        show = processShow(metadata)

        artist_id = getArtistId(show['artist_identifier'])
        if not artist_id:
            print "ADDING MISSING ARTIST"
            artist_meta = getMeta(show['artist_identifier'])
            # print artist_meta
            artist = processCollection(artist_meta)
            r = postArtist(artist)
            # artist_id = getArtistId(show['artist_identifier'])    
            # print r, r.raw_body
            # pritn type(r.raw_body)
            # print json.loads(r.raw_body)
            artist_id = r.body['_id']
        
        print artist_id
        try:
            show['artist'] = artist_id
            # time.sleep(5)
            postShow(show)
        except:
            print "NO ARTIST ID FOUND"
            raise
        # process as show of artist

if __name__ == '__main__':
    args = sys.argv[1]
    main(args)