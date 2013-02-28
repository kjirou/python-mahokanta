from webob.dec import wsgify

@wsgify
def dump(request):
    
    text = request.as_text()
    
    # To console
    print('--------')
    print(text)
    print('--------')

    # To browser
    request.response.content_type = 'text/plain'
    return text
