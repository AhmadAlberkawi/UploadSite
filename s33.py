#!/usr/bin/python3

from bottle import route, run , template, request
import requests, boto3
from boto3 import resource 

import time
import os
import uuid

@route('/')
def home(success_messages=None):
    # Get all entries from table
    r = table.scan()
    items = r['Items']
    return template('home.tpl', name='BoTube', items=items)


# ...
# This is a sniplet only!!!
@route('/upload', method='GET')
def do_upload_get():
    return template('home.tpl', name='Upload Image')


@route('/upload', method='POST')
def do_upload_post():
    category = request.forms.get('category')
    description = request.forms.get('description')	
    upload = request.files.get('file_upload')

    # Check for errors
    error_messages = []
    if not upload:
        error_messages.append('Please upload a file.')
    if not category:
        error_messages.append('Please enter a category.')

    try:
        name, ext = os.path.splitext(upload.filename)
        if ext not in ('.png', '.jpg', '.jpeg'):
            error_messages.apend('File Type not allowed.')
    except:
        error_messages.apend('Unknown error.')

    if error_messages:
        return template('home.tpl', name='Upload Image', error_messages=error_messages,items=[])

    # Save to /tmp folder
    upload.filename = name + '_' + time.strftime("%Y%m%d-%H%M%S") + ext
    upload.save('/tmp/images/' + upload.filename)

    # Upload to S3
    data = open('/tmp/images/' + upload.filename, 'rb')

    s3 = boto3.resource('s3')	

    s3.Bucket('learntechno').put_object(Key=upload.filename,
                                                       Body=data,
                                                       ACL='public-read')

    # Write to DynamoDB
    table.put_item(Item={'id': uuid.uuid4().int >> 64,
                         'filename': upload.filename,
                         'category': category,
                         'description': description,
                         'time_created': time.strftime("%Y%m%d-%H%M%S")})

    # Return template
    return template('upload_success.tpl', name='Upload Image')

# ....


if __name__ == '__main__':
    # Connect to DB
    dynamodb_resource = resource('dynamodb', region_name='us-east-1')
    table = dynamodb_resource.Table('learntech')

    run(host=requests.get('http://169.254.169.254/latest/meta-data/public-hostname').text, port=80)


