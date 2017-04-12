"""
BRCK Control Panel
Copyright (c) 2016, BRCK Inc
All Rights Reserved
"""

import mimetypes
import os

from moja import create_app
# Instantiate the Flask application and Babel object
app = create_app(os.getenv('FLASK_CONFIG') or 'default')

if __name__ == '__main__':
    mimetypes.add_type('image/svg+xml', '.svg', True)
    # Start the application
    app.run(host="127.0.0.1", port=8050, debug=True)
