# teakwood

A archive.org LMA interface. Backend written in MongoDB, Redis, and Flask along with a messaging queue in Python-RQ. Frontend is AngularJS, served by flask.

Requires Fig. 

After cloning, fig up is all you need to start the environment. 


API (currently served on localhost:8081)
/artists
/artists/<artist_name>
/shows/<artist_name/
/shows/<artist_name>/<date>
/shows 
