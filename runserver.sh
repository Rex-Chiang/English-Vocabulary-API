#!/bin/bash

gunicorn -c gunicorn.conf.py config.wsgi  --timeout 300 --keep-alive 50