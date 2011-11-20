#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.


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
    """
    Encode Video 
    
    Required: content_type, title, sourcefile
    Optional: blurb, callback
    
    Callback should be a url on your servers that we can call to tell you a 
    job is complete.
    eg. http://example.com/job_callback
    """
    
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
    
def edit_player(uuid, **kwargs):
    """
    Edit MoovAtom Player.
    
    You can specify one, a few, or all of the parameters.  You don't 
    need to specify every single parameter if you just want to change
    a couple things.
    
    Example kwargs:
    player_data = {
        'height': 480,
        'width': 720,
        'auto_play': False,
        'sharing_enabled': True,
        'show_hold_image': True,

        #Example watermarks, only use one or the other
        #Example s3 Watermark.
        #'watermark': 'http://XXXXXXXXXXXXXXXXXXXX:YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY@your-bucket-name.s3.amazonaws.com/path_to/watermark.png', 
        #Example non cloud watermark.
        #'watermark': 'http://example.com/path_to/watermark.png',

        'watermark_url': 'http://www.google.com',
        'show_watermark': True,
        'watermark_opacity': 0.8,
        'background_color': '#000000',
        'duration_color': '#FFFFFF',
        'buffer_color': '#6C9CBC',
        'volume_color': '#000000',
        'volume_slider_color': '#000000',
        'button_color': '#889AA4',
        'button_over_color': '#92B2BD',
        'time_color': '#01DAFF',
    }
    """
    
    edit_player_url = '%s/edit_player.%s' % (BASE_URL, EMITTER)
    post_data.update(kwargs)
    post_data.update({'uuid': uuid})
    return api_request(edit_player_url, post_data)
    
def status(uuid):
    """
    Encoding Status
    
    This will return a percentage complete of an encoding job.  If the job is
    complete, it will return that it is.
    """
    
    status_url = '%s/status.%s' % (BASE_URL, EMITTER)
    post_data.update({'uuid': uuid})
    return api_request(status_url, post_data)
    
def cancel(uuid):
    """
    Cancel Job
    
    This will cancel a running encode job.  It has no effect after the job is 
    complete.
    """
        
    cancel_url = '%s/cancel.%s' % (BASE_URL, EMITTER)
    post_data.update({'uuid': uuid})
    return api_request(cancel_url, post_data)
    
def detail(uuid):
    """
    Media Details
    
    This will return a strucutre that includes all the resources on MoovAtom's
    servers for a given media uuid.
    """
    
    detail_url = '%s/detail.%s' % (BASE_URL, EMITTER)
    post_data.update({'uuid': uuid})
    return api_request(detail_url, post_data)

def api_request(url, post_data):
    params = urllib.urlencode(post_data)
    response = urllib.urlopen(url, params).read()   
    return response
    


    


    
    