#!/bin/sh
gunicorn -c gunicorn.conf.py d08.wsgi