from eve import Eve
import datetime
import sys

artist_schema = {
        'name': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 100,
            'required': True,
            'unique': True                
        },
        'display_name': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 100
        },
        'identifier': {
            'type': 'string'
        },
        'rights': {
            'type': 'string'
        },
        'addeddate': {
            'type': 'datetime'
        },
        'refreshcount': {
            'type': 'integer'
        }
}

show_schema = {
        'artist': {
            'type': 'objectid',
            'required': True,
            'data_relation': {
                'resource': 'artists',
                'embeddable': True
            }
        },                                                                                          
        'identifier': {
            'type': 'string',
            'required': True,
            'unique': True,
            'minlength': 1,
            'maxlength': 100
            },                                                                                           
        'title': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 100
            },                                                                                           
        'location': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 100
            },                                                                                           
        'venue': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 100
            },                                                                                           
        'date': {
            'type': 'datetime',
            'required': True
            },   
        'addeddate': {
            'type': 'datetime'
            },   
        'updatedate': {
            'type': 'datetime'
            },   
        'description': {
            'type': 'string'
            },                                                                           
        'taper': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 100
            },      
        'transferer': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 100
            },
        'creator': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 100
            },                             
        'uploader': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 100
            },      
        'lineage': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 100
            },      
        'source': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 100
            },  
        'files' : {
            'type': 'list',
            'schema': {   
                'type': 'dict',
                'schema': {
                    'file_name': {
                        'type': 'string'
                        # 'required': True
                    },
                    'file_format': {
                        'type': 'string'
                        # 'required': True
                    },
                    'title': {
                        'type': 'string'
                    },
                    'track': {
                        'type': 'integer'
                    },
                    'length': {
                        'type': 'string'
                    },
                    'bitrate': {
                        'type': 'integer'
                    },
                    'mp3_hq_bit': {
                        'type': 'integer'
                    },
                    'mp3_bit': {
                        'type': 'integer'
                    }
                }
            }   
        },
        'comments' : {
            'type': 'list',
            'schema': {   
                'type': 'dict',
                'schema': {
                    'date': {
                        'type': 'datetime'
                        # 'required': True
                    },
                    'title': {
                        'type': 'string'
                    },
                    'content': {
                        'type': 'string'
                    },
                    'reviewer': {
                        'type': 'string'
                    },
                    'rating': {
                        'type': 'integer'
                    }
                }
            }
        } # end comments
    }

artists = {
    'url': 'artists',
    'item_title': 'artist',
    'id_field': '_id',
    'resource_methods': ['GET', 'POST'],
    'additional_lookup': {
       'url': 'regex("[\w]+")',
       'field': 'name'
    },
    'schema': artist_schema

    # 'datasource': {
    #     'source': 'artists',
    #     'projection': {
    #         'name': 1,
    #         'count': 1
    #     }
    # }
}

shows = {
    'url': 'shows',
   'item_title': 'show',
    'resource_methods': ['GET', 'POST'],
    'additional_lookup': {
       'url': 'regex("[\w]+")',
       'field': 'identifier'
    },    
    'schema': show_schema
}

artists_shows = {
    "url": "artists/<regex('[a-f0-9]{24}'):artist>/shows",
    # 'url': 'artists/<regex("[\w]+"):artist>/shows',
    'item_title': 'show',
    'item_url': 'regex("[\w]+")',
    'item_lookup': True,
    'item_lookup_field': 'identifier',
    # 'id_field': 'identifier',
    'schema': show_schema,
    'datasource': {
        'source': 'shows'
        }
    #     'projection': {
    #         'name': 1,
    #         'shows': 1
    #         }
    # }
}

my_settings = {
    # 'SERVER_NAME': None,
    'MONGO_HOST': 'database',
    'MONGO_PORT': 27017,
    'MONGO_DBNAME': 'teakwood',
    'DOMAIN': {
        'artists': artists,
        'shows': shows,
        'test': artists_shows
    },
    'X_DOMAINS': '*',
    'DEBUG': True,
    'HATEOAS': False,
    # 'DATE_FORMAT': '%Y-%M-%D %H:%M:%S',
    'RESOURCE_METHODS': ['GET', 'POST'],
    'ITEM_METHODS': ['GET', 'PATCH', 'PUT', 'DELETE']
}
# SERVER_NAME = None

def count_shows(response):   
    pass

app = Eve(settings=my_settings)
app.on_fetched_resource_artists += count_shows

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)