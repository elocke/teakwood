# teakwood

A archive.org LMA interface. Backend written in MongoDB, Redis, and Flask along with a messaging queue in Python-RQ. Frontend is AngularJS, served by flask.

Requires [Docker](http://docker.com). 

After cloning, run docker-compose up and the environment will start.  


### API (currently served on localhost:8081)
- /artists
- /artists/<artist_name>
- /shows/'artist_name'/
- /shows/'artist_name'/'date'
- /shows 

