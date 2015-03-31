# teakwood

A archive.org LMA interface. Backend written in MongoDB, Redis, and Flask along with a messaging queue in Python-RQ. Frontend is AngularJS, served by flask.

Requires [Docker](http://docker.com). 

After cloning, run docker-compose up and the environment will start.  

Bash shell is accessible by running docker-compose run workers /bin/bash


### API (currently served on localhost:8080/api)
- /artists [GET, POST]
- /artists/<artist_name>/shows [GET]
- /artists/<_id> [GET, POST]
- /artists/<_id>/shows [GET, POST]
- /shows/ [GET, POST]
- /shows/<_id> [GET, POST]

[EVE](http://python-eve.org) for reference

### Angular (http://localhost:8080/
Main View - /
Artist View (List of shows) - /artist/<_id>
Show View (Single show) - /show/<_id>
