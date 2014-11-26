import datetime

from flask import url_for
from app import db

class Artist(db.Document):
  name = StringField(required=True)
  website = URLField()

  meta = {
    'indexes': ['name']
  }

class Show(db.Document):
  meta = {'allow_inheritance': True}

  creator = ReferenceField(name)

  title = StringField()
  venue
  coverage = StringField()
  date = DateTimeField()
  addeddate = DateTimeField()
  publicdate = DateTimeField()

  identifier = StringField()


  server = StringField()
  url = StringFieldd()  # Combine server & dir



  #

  # Lineage Info
  taper = StringField
  transferer
  uploader
  lineage

  # Files
  files = ListField(EmbeddedDocumentField(File))

  # Comments
  comments = ListField(EmbeddedDocumentField(Comment))




  class File(EmbeddedDocument):
    file_name
    file_format
    source
    title
    track
    length
    bitrate
    size

  class Comment(EmbeddedDocument):
    date = DateTime()
    id = Int
    title = StringField(max_length=180)
    rating = Int
    author = StringField(max_length=60)
    content = StringField()

