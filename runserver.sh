#!/bin/bash

gunicorn -c gunicorn.conf.py config.wsgi --log-level DEBUG --timeout 300 --keep-alive 50