from firebase import firebase

def get_top_story():
    fb = firebase.FirebaseApplication('https://hacker-news.firebaseio.com', None)
    top_id = fb.get('/v0/topstories', None)[0]
    result = fb.get('/v0/item/%d' % top_id, None)
    return result['title'], result['url']
