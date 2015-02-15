import datetime
from flask import url_for
from app import db

class Artist(db.Document):
  meta = {
    'ordering': ['name']
  }
  name = db.StringField(required=True, unique=True)
  display_name = db.StringField()
  shows = db.ListField(db.EmbeddedDocumentField('Show'))
  website = db.URLField()

  def check_artist(self, artist):
    for names in self.name:
      if names == artist:
        print "hello"


class Show(db.EmbeddedDocument):
  meta = {
    'allow_inheritance': False,
    'indexes': ['year']}

  # INTERNAL FIELDS
  importdate = db.DateTimeField(default=datetime.datetime.now, required=True)
  refreshdate = db.DateTimeField(default=datetime.datetime.now, required=True)  # TODO: maybe a trigger on updates?
  refreshcount = db.IntField(default=0, required=True)  # counter of times refreshed
  server = db.StringField(required=True)  # server
  url = db.StringField(required=True)  # Combine server & dir

  # ETREE FIELDS
  identifier = db.StringField(required=True, unique=True)  # unique etree identifier
  # creator = db.ReferenceField(Artist, reverse_delete_rule=db.DENY)  # creator

  title = db.StringField(required=True)  # title
  location = db.StringField()  # location (city, st)
  venue = db.StringField()  # venue
  # year = db.IntField()  # year TODO parse from date
  date = db.DateTimeField(required=True)  # date played
  addeddate = db.DateTimeField()  # addeddate
  updatedate = db.ListField(db.DateTimeField())  # array of updatedates
  description = db.StringField()

  # --Recording Info
  taper = db.StringField()  # taper
  transferer = db.StringField()  # transferer
  uploader = db.StringField()  # uploader (email)
  lineage = db.StringField()  # lineage
  source = db.StringField()  # source

  # Files
  files = db.ListField(db.EmbeddedDocumentField('File'), required=True)

  # Comments
  comments = db.ListField(db.EmbeddedDocumentField('Comment'))


class File(db.EmbeddedDocument):
  meta = {
    'ordering': ['track']
  }
  file_name = db.StringField(required=True)  # name (filename)
  file_format = db.StringField()  # format -- VBRMP3 / VBRZIP
  title = db.StringField()  #
  track = db.IntField()  # track number
  length = db.StringField() # convert to ms


class Comment(db.EmbeddedDocument):
  date = db.DateTimeField()  # createdate
  title = db.StringField()  # reviewtitle
  content = db.StringField()  # reviewbody
  reviewer = db.StringField()  # reviewer
  rating = db.IntField ()  # stars


