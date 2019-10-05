#!/bin/bash

set -e

export FLASK_APP=run

flask db upgrade
flask db migrate

python /app/run.py
