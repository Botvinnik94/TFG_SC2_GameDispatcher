import re
import urllib.request
import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

def _urlToBucketPath (url):
    """
    Convert a Firebase HTTP URL to a (bucket, path) tuple, 
    Firebase's `refFromURL`.
    """
    bucket_domain = '([A-Za-z0-9.\\-]+)'
    is_http = not url.startswith('gs://')

    if is_http:
        path = '(/([^?#]*).*)?$'
        version =  'v[A-Za-z0-9_]+'
        rex = (
            '^https?://firebasestorage\\.googleapis\\.com/' +
            version + '/b/' + bucket_domain + '/o' + path)
    else:
        gs_path = '(/(.*))?$'
        rex = '^gs://' + bucket_domain + gs_path

    matches = re.match(rex, url, re.I)
    if not matches:
        raise Exception('URL does not match a bucket: %s' % url)

    bucket, _, path = matches.groups()

    if is_http:
        path = urllib.parse.unquote(path)

    return (bucket, path)


cred = credentials.Certificate('./sc2-arena-firebase-adminsdk.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'sc2-arena.appspot.com'
})

def get(local_path, remote_url):
    """Saves a file in local filesystem from the Firebase Storage Service"""
    remote_path = _urlToBucketPath(remote_url)[1]
    bucket = storage.bucket()
    blob = bucket.blob(remote_path)
    url = blob.generate_signed_url(datetime.timedelta(seconds=300), method='GET')
    urllib.request.urlretrieve(url, local_path)

def put(local_path, remote_path):
    """Saves a file in the Firebase Storage Service from the local filesystem"""
    bucket = storage.bucket()
    blob = bucket.blob(remote_path)
    with open(local_path, "rb") as file_obj:
        blob.upload_from_file(file_obj)
    return blob.generate_signed_url(datetime.timedelta(seconds=300), method='GET').split('?')[0]