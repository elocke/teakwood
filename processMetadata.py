from app.models import *
import ujson
import os
import argparse
from datetime import datetime
from operator import itemgetter


class ImportShow(object):
    """Accepts single Archive.org metadata and parses it for
    the Teakwood project's db"""

    def __init__(self, object):
        self.json = self._open_file(object)

    def _open_file(self, fileName):
        try:
            f = open(fileName, 'r')
            json = f.read()
            f.close()
            print 'Success: read file'
            return json
        except IOError:
            print 'Error: cannot find file'

    def parse_json(self):
        jdict =  ujson.loads(self.json)
        sdict = {'show': {}
            }

        # Metadata
        meta = jdict['metadata']
        sdict['artist'] = meta['creator']

        # Internal info
        sdict['show']['server'] = jdict['server']
        sdict['show']['dir'] = jdict['dir']
        sdict['show']['url'] = 'http://' + jdict['server'] + jdict['dir']

        #
        sdict['show']['identifier'] = meta['identifier']
        # sdict['show']['creator'] = meta['creator']
        sdict['show']['title'] = meta['title']
        if 'coverage' in meta:
            sdict['show']['location'] = meta['coverage']
        if 'venue' in meta:
            sdict['show']['venue'] = meta['venue']
        if 'year' in meta:
            sdict['show']['year'] = meta['year']

        if 'date' in meta:
            sdict['show']['date'] = datetime.strptime(meta['date'], "%Y-%m-%d")  # date formatting? xxxx-xx-xx
        if 'addeddate' in meta:
            sdict['show']['addeddate'] = datetime.strptime(meta['addeddate'], "%Y-%m-%d %H:%M:%S") # xxxx-xx-xx xx:xx:xx

        if 'updatedate' in meta:
            sdict['show']['updatedate'] = []
            if isinstance(meta['updatedate'], list):
                for date in meta['updatedate']:
                    sdict['show']['updatedate'].append(datetime.strptime(date, "%Y-%m-%d %H:%M:%S")) # xxxx-xx-xx xx:xx:xx
            else:
                sdict['show']['updatedate'].append(datetime.strptime(meta['updatedate'], "%Y-%m-%d %H:%M:%S")) # xxxx-xx-xx xx:xx:xx

        if 'description' in meta:
            sdict['show']['description'] = meta['description']

        if 'taper' in meta:
            sdict['show']['taper'] = meta['taper']
        if 'transferer' in meta:
            sdict['show']['transferer'] = meta['transferer']
        if 'uploader' in meta:
            sdict['show']['uploader'] = meta['uploader']
        if 'lineage' in meta:
            sdict['show']['lineage'] = meta['lineage']
        if 'source' in meta:
            sdict['show']['source '] = meta['source']

        if 'files' in jdict:
            sdict['show']['files'] = []
            temp_list = []
            files = jdict['files']
            for f in  files:
                tempd = {}
                if f['format'] in ['VBR MP3', 'VBR ZIP']:
                    tempd['file_name'] = f['name']
                    tempd['file_format'] = f['format']
                    if f['format'] == 'VBR MP3':
                        if 'title' in f:
                            tempd['title'] = f['title']
                        if 'track' in f:
                            tempd['track'] = f['track']
                        else:
                            # TODO: regex match d1tXX.mp3
                            pass
                        if 'length' in f:
                            tempd['length'] = f['length']  # convert to ms
                    temp_list.append(tempd)
            newlist = sorted(temp_list, key=itemgetter('file_name'))
            sdict['show']['files'] = newlist

        if 'reviews' in jdict:
            sdict['show']['comments'] = []
            reviews = jdict['reviews']
            for review in reviews:
                tempd = {}
                tempd['date'] = review['createdate']
                tempd['title'] = review['reviewtitle']
                tempd['content'] = review['reviewbody']
                tempd['reviewer'] = review['reviewer']
                tempd['rating'] = review['stars']
                sdict['show']['comments'].append(tempd)

        return sdict


    def commit(self, odict):
        artist = Artist()
        show = Show()
        artist.name = odict.pop('artist')

        show_meta = odict.pop('show')

        for k, v in show_meta.iteritems():
            # print k, v
            if k == 'updatedate':
                for i in v:
                    show.updatedate.append(i)

            elif k == 'files':
                print 'files'
                # what happens when it's all FLACs? keep the doc and hide or exlude as source?
                # for f in show_meta.pop('files'):
                for f in v:
                    f_obj = File()
                    # f_obj.file_name = f['file_name']
                    # f_obj.file_format = f['file_format']
                    for i, j in f.iteritems():
                        setattr(f_obj, i, j)
                    show.files.append(f_obj)

            elif k == 'comments':
                print 'comments'
                for f in v:
                    f_obj = Comment()
                    for i, j in f.iteritems():
                        setattr(f_obj, i, j)
                    show.comments.append(f_obj)
                # calculate avg rating from # of reviews and rating?


            else:
                # print k, v
                setattr(show, k, v)

        artist.shows.append(show)
        artist.save()


def main():
    parser = argparse.ArgumentParser(description='Parse archive.org metadata into mongodb')
    parser.add_argument('filename')
    args = parser.parse_args()
    filename = os.path.join('/home/evanl/Projects/teakwood', args.filename)
    # print filename
    show = ImportShow(filename)
    odict = show.parse_json()
    print odict
    show.commit(odict)

if __name__ == "__main__":
    main()

