import os
import sys
import subprocess
import requests
import ssl
import random
import string
import json

from flask import jsonify
from flask import Flask
from flask import request
from flask import send_file
import traceback

from app_utils import blur
from app_utils import download
from app_utils import generate_random_filename
from app_utils import clean_me
from app_utils import clean_all
from app_utils import create_directory
from app_utils import get_model_bin
from app_utils import get_multi_model_bin

import re

try:  # Python 3.5+
    from http import HTTPStatus
except ImportError:
    try:  # Python 3
        from http import client as HTTPStatus
    except ImportError:  # Python 2
        import httplib as HTTPStatus


app = Flask(__name__)


@app.route("/detect", methods=["POST"])
def process():

    try:
        text = request.json["text"]
   
        results = []

        matches = regex.finditer(text)

        for matchNum, match in enumerate(matches, start=1):
    
            out = "Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group())
            results.append({
                'verbose': out,
                'matchNum': matchNum,
                'match': match.group(),
                'start': match.start(),
                'end': match.end()
                })
    
        return json.dumps(results), 200

    except:
        traceback.print_exc()
        return {'message': 'input error'}, 400



if __name__ == '__main__':
    global regex

    regex = re.compile(r'[\w\-][\w\-\.]+@[\w\-][\w\-\.]+[a-zA-Z]', re.IGNORECASE|re.MULTILINE)


    port = 5000
    host = '0.0.0.0'

    app.run(host=host, port=port, threaded=True)

