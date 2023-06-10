import os
import uuid

import boto3

from fastapi import UploadFile

class Uploader:
    def __init__(self):
        ENDPOINT_URL = os.environ['ENDPOINT_URL']
        AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
        REGION_NAME = os.environ['REGION_NAME']
        AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
        self.bucket = 'video.online'
        self._s3 = boto3.client('s3',
                            endpoint_url=ENDPOINT_URL,
                            aws_access_key_id=AWS_ACCESS_KEY_ID,
                            region_name=REGION_NAME,
                            aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

    def upload_file(self, video: UploadFile, id):
        key = video.filename + '/' + str(id)
        self._s3.upload_fileobj(video.file, self.bucket, key, ExtraArgs={
            'ContentType': video.headers.get('content-type')
        })

        url = 'https://storage.yandexcloud.net/video.online/' + key
        return url
