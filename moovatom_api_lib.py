import urllib

USER_NAME = 'YOUR_MOOVATOM_USER_NAME'
USER_KEY = 'YOUR_MOOVATOM_API_KEY'
BASE_URL = 'https://www.moovatom.com/api/v2'
EMITTER = 'xml'  #xml or json

post_data = {
    'username': USER_NAME,
    'userkey': USER_KEY,
}
     
def encode(source_file, file_type, callback_url, title, blurb):
    encode_job_url = '%s/encode.%s' % (BASE_URL, EMITTER)
    post_data.update(
        {
            'content_type': file_type,
            'title': title,
            'blurb': blurb,
            'sourcefile': source_file,
            'callback': callback_url
        }
    )
    return api_request(encode_job_url, post_data)
    
def status(uuid):
    status_url = '%s/status.%s' % (BASE_URL, EMITTER)
    post_data.update({'uuid': uuid})
    return api_request(status_url, post_data)
    
def cancel(uuid):
    cancel_url = '%s/cancel.%s' % (BASE_URL, EMITTER)
    post_data.update({'uuid': uuid})
    return api_request(cancel_url, post_data)
    
def detail(uuid):
    detail_url = '%s/detail.%s' % (BASE_URL, EMITTER)
    post_data.update({'uuid': uuid})
    return api_request(detail_url, post_data)

def api_request(url, post_data):
    params = urllib.urlencode(post_data)
    response = urllib.urlopen(url, params).read()   
    return response
    

    