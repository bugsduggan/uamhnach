#!/usr/bin/env python

from uamhnach import app


import logging
logging.addLevelName(5, 'DEVEL')
logging.basicConfig(filename=app.config['LOGFILE'])
LOG = logging.getLogger()
LOG.setLevel('DEVEL' if app.config['DEBUG'] is 'DEVEL'
             else app.config['LOGLVL'])
LOG.info("Logging at level %s", 'DEVEL' if app.config['DEBUG'] is 'DEVEL'
        else app.config['LOGLVL'])


dbg = True if app.config['DEBUG'] is 'DEVEL' else app.config['DEBUG']

app.run(debug=dbg)
