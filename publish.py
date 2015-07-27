#!/usr/bin/env python

import os
from linkedin import linkedin
from linkedin.models import AccessToken
from fetch import get_top_story

QUOTES = [
    'You guys should reall check this out!',
    'came across this great link',
    'this could apply to LeadGenius!',
    'glad I found this',
    "you won't believe #6!"
]

def get_authentication():
    APP_KEY = os.environ.get('LINKEDIN_APP_KEY')
    APP_SECRET = os.environ.get('LINKEDIN_APP_SECRET')
    #AUTH_CODE = os.environ.get('LINKEDIN_AUTH_CODE')
    AUTH_TOKEN = os.environ.get('LINKEDIN_AUTH_TOKEN')
    RETURN_URL = 'http://localhost:5000/'
    SCOPES = ['r_basicprofile', 'w_share']

    authentication = linkedin.LinkedInAuthentication(
        APP_KEY,
        APP_SECRET,
        RETURN_URL,
        SCOPES)

    #print authentication.authorization_url
    #import ipdb; ipdb.set_trace()

    #authentication.authorization_code = AUTH_CODE
    #token = authentication.get_access_token()
    authentication.token = AccessToken(access_token=AUTH_TOKEN, expires_in=60)
    #import ipdb; ipdb.set_trace()
    return authentication

def publish(authentication):
    application = linkedin.LinkedInApplication(authentication)

    title, url = get_top_story()
    application.submit_share(
        '',    # description
        title, # title
        None,
        url,   # link URL
        None)  # thumbnail URL

if __name__ == "__main__":
    authentication = get_authentication()
    publish(authentication)
