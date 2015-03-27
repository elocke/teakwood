from datetime import datetime
# from flask import url_for
# from app import db
from mongoengine import *
from mongoengine import signals
import logging

def handler(event):
    """Signal decorator to allow use of callback functions as class decorators."""

    def decorator(fn):
        def apply(cls):
            event.connect(fn, sender=cls)
            return cls

        fn.apply = apply
        return fn

    return decorator

@handler(signals.pre_save)
def update_count(sender, document, **kwargs):
    # document.date_count = 192
    countres = Artists._get_collection().aggregate([{'$match': {'name' : document.name}}, {'$project': {'item': {'name': '$name'}, 'count': { '$size': "$shows" }} }])
    for x in Artists.objects(name = document.name):
      print x
      # for v in x:
        # print v
    # document.date_count = count
    if countres['ok'] == 1:
      print 'im doing shit'
      document.count = countres['result'][0]['count']
    # print document


@update_count.apply
class Artists(Document):
  # @classmethod
  # def pre_save(cls, sender, document, **kwargs):
  #     print 'fuck you im a train'
  #     document.date_count = 999
  #     logging.debug("Pre Save: %s" % document.name)

  # @classmethod
  # def post_save(cls, sender, document, **kwargs):
  #     logging.debug("Post Save: %s" % document.name)
  #     print 'fuck you im a train'

  #     if 'created' in kwargs:
  #         if kwargs['created']:
  #             logging.debug("Created")
  #         else:
  #             logging.debug("Updated")

  meta = {
    'ordering': ['name']
  }
  name = StringField(required=True, unique=True)
  display_name = StringField()
  shows = ListField(EmbeddedDocumentField('Show'))
  website = URLField()
  date_count = IntField()
  count = IntField()

  def check_artist(self, artist):
    for names in self.name:
      if names == artist:
        print "hello"


class Show(EmbeddedDocument):
  meta = {
    'allow_inheritance': False,
    'indexes': ['year']}

  # INTERNAL FIELDS
  importdate = DateTimeField(default=datetime.now, required=True)
  refreshdate = DateTimeField(default=datetime.now, required=True)  # TODO: maybe a trigger on updates?
  refreshcount = IntField(default=0, required=True)  # counter of times refreshed
  server = StringField(required=True)  # server
  url = StringField(required=True)  # Combine server & dir

  # ETREE FIELDS
  identifier = StringField(required=True, unique=True)  # unique etree identifier
  # creator = ReferenceField(Artist, reverse_delete_rule=DENY)  # creator

  title = StringField(required=True)  # title
  location = StringField()  # location (city, st)
  venue = StringField()  # venue
  # year = IntField()  # year TODO parse from date
  date = DateTimeField(required=True)  # date played
  addeddate = DateTimeField()  # addeddate
  updatedate = ListField(DateTimeField())  # array of updatedates
  description = StringField()

  # --Recording Info
  taper = StringField()  # taper
  transferer = StringField()  # transferer
  uploader = StringField()  # uploader (email)
  lineage = StringField()  # lineage
  source = StringField()  # source

  # Files
  files = ListField(EmbeddedDocumentField('File'), required=True)

  # Comments
  comments = ListField(EmbeddedDocumentField('Comment'))


class File(EmbeddedDocument):
  meta = {
    'ordering': ['track']
  }
  file_name = StringField(required=True)  # name (filename)
  file_format = StringField()  # format -- VBRMP3 / VBRZIP
  title = StringField()  #
  track = IntField()  # track number
  length = StringField() # convert to ms


class Comment(EmbeddedDocument):
  date = DateTimeField()  # createdate
  title = StringField()  # reviewtitle
  content = StringField()  # reviewbody
  reviewer = StringField()  # reviewer
  rating = IntField ()  # stars



# signals.pre_save.connect(Artists.pre_save, sender=Artists)