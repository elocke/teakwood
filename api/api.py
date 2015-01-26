



artist_schema = {
    # by default the standard item entry point is defined as
    # '/people/<ObjectId>/'. We leave it untouched, and we also enable an
    # additional read-only entry point. This way consumers can also perform GET
    # requests at '/people/<lastname>/'.
    'additional_lookup': {
       'url': 'regex("[\w]+")',
       'field': 'name'
    },

    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/nicolaiarocci/cerberus) for details.
    'schema': {
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
        'shows': {
            'type': 'dict',
            'schema': {
                'importdate': {
                    'type': 'datetime',
                    'required': True,
                    'default': datetime.datetime.now()
                    },
                 'refreshdate': {
                    'type': 'datetime'
                    },
                'refreshcount': {
                    'type': 'int',
                    'min': 0,
                    'max': 100
                    },
                'server': {
                    'type': 'string',
                    'minlength': 1,
                    'maxlength': 100
                    },
                'url': {
                    'type': 'string',
                    'minlength': 1,
                    'maxlength': 100
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
                'files': {
                    'type': 'dict',
                    'schema': {
                        'file_name': {
                            'type': 'string',
                            'required': True
                        },
                        'file_format': {
                            'type': 'string',
                            'required': True
                        },
                        'title': {
                            'type': 'string'
                        },
                        'track': {
                            'type': 'int'
                        },
                        'length': {
                            'type': 'string'
                        }
                    }
                },                                                                                                                              
                'comments': {
                    'type': 'dict',
                    'schema': {
                        'date': {
                            'type': 'datatime',
                            'required': True
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
                            'type': 'int'
                        }
                    }
                }
            }
        }                  
    }
}

# default eve settings
my_settings = {
    'MONGO_HOST': 'database',
    'MONGO_PORT': 27017,
    'MONGO_DBNAME': 'teakwood',
    'DOMAIN': {
        'artists': artist_schema
    },
    'URL_PREFIX': 'api'
}


# init extension
# ext = EveMongoengine(app)
# register model to eve
# esxt.add_model(Artist)

# app = Eve(settings=my_settings)


