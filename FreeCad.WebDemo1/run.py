"""
This script runs the Flask ServerApp application using a development server.
"""

from ServerApp.FlaskServer import flaskserv

if __name__ == '__main__':

    # Run Flask as a development server
    flaskserv.get_free_port()
    flaskserv.start_async()
