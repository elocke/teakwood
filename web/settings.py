artist_schema = {
        'name': {
            'type': 'string',
            'minlength': 1,
            # 'maxlength': 100,
            'required': True,
            'unique': True                
        },
        'display_name': {
            'type': 'string',
            'minlength': 1
            # 'maxlength': 100
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
        },
        'show_count': {
            'type': 'integer'
        },
        'years': {
            'type': 'list'
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
            'minlength': 1
            # 'maxlength': 100
            },        
        'artist_identifier': {
            'type': 'string',
            'required': True,
            'minlength': 1
            # 'maxlength': 100
            },                                                                                                           
        'title': {
            'type': 'string'
            # 'minlength': 1,
            # 'maxlength': 100
            },                                                                                           
        'location': {
            'type': 'string'
            # 'minlength': 1,
            # 'maxlength': 100
            },                                                                                           
        'venue': {
            'type': 'string'
            # 'minlength': 1,
            # 'maxlength': 100
            },                                                                                           
        'date': {
            'type': 'datetime',
            'required': True
            },   
        'year': {
            'type': 'integer'
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
            'type': 'string'
            # 'minlength': 1,
            # 'maxlength': 100
            },      
        'transferer': {
            'type': 'string'
            # 'minlength': 1,
            # 'maxlength': 100
            },
        'creator': {
            'type': 'string'
            # 'minlength': 1,
            # 'maxlength': 100
            },                             
        'uploader': {
            'type': 'string'
            # 'minlength': 1,
            # 'maxlength': 100
            },      
        'lineage': {
            'type': 'string'
            # 'minlength': 1,
            # 'maxlength': 100
            },      
        'source': {
            'type': 'string'
            # 'minlength': 1,
            # 'maxlength': 100
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
       'field': 'identifier'
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
        'source': 'shows',
        'projection': {
            'identifier': 1,
            'venue': 1,
            'date': 1,
            'title': 1,
            'location': 1
        }
    }
}

artists_years = {
    "url": "artists/<regex('[a-f0-9]{24}'):_id>/years",
    'schema': artist_schema,
    'datasource': {
        'source': 'artists',
        'projection': {
            'years': 1
        }
    }
}


# 'SERVER_NAME': None,
MONGO_HOST = 'database'
MONGO_PORT = 27017
MONGO_DBNAME = 'teakwood'
X_DOMAINS = '*'
DEBUG = True
HATEOAS = False
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
RESOURCE_METHODS = ['GET', 'POST']
ITEM_METHODS =['GET', 'PATCH', 'PUT', 'DELETE']
DOMAIN = {
    'artists': artists,
    'shows': shows,
    'artist_shows': artists_shows
} 
URL_PREFIX = 'api'
X_ALLOW_CREDENTIALS = True