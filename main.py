from flask import Flask, request, render_template, redirect, url_for
from __init__ import *
import os


if __name__ == '__main__':
    app = create_app()  
    SECRET_KEY = os.urandom(32)
    app.config['SECRET_KEY'] = SECRET_KEY
    app.run(host='127.0.0.1', port=8080, debug=True)