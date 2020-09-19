"""
The flask server.
"""

import threading
from os import environ
from flask import Flask
from os import path

class FlaskServer(object):

    def __init__(self):
        """Class Initializer"""

        # Server host to listen on
        self.HostName = 'localhost'
        # Port to listen on
        self.Port = 0
        # thread used for running async
        self.flaskthread:threading.Thread = None
        # Flask Application
        self.app = Flask(
                        __name__,
                        template_folder="Views",
                        static_folder=path.abspath('wwwroot'),
                        static_url_path='/')

    def get_free_port(self):
        """Get a free port to host on"""
        try:
            self.Port = int(environ.get('SERVER_PORT', '5555'))
        except ValueError:
            self.Port = 5555

    def start(self):
        """Start the Flask server, this blocks the thread"""
        self.app.run(self.HostName, self.Port)

    def start_async(self):
        """Start the Flask server async, non blocking"""
        self.flaskthread = threading.Thread(target=self.start)
        self.flaskthread.start()

    def stop_async(self):
        if self.flaskthread is not None:
            self.app.do_teardown_appcontext()

# Declare a singleton class
flaskserv = FlaskServer()

# These represent the controllers / handlers for the Flask application pages
import ServerApp.Controllers


# If called directly from the command-line,
if __name__ == '__main__':
    flaskserv.get_free_port()
    flaskserv.start_async()
