"""Run the service."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from t206api.app import create_app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', debug=True)
