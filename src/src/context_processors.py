from django.conf import settings

def bootstrap(request):
    return {
        'is_user' : request.session.get('is_user'),
        'APP_NAME' : settings.APP_NAME,
        'MEDIA_URL' : '/media/',
    }

def language_code(request):
    return {"LANGUAGE_CODE": "request.LANGUAGE_CODE"}

def get_cookie(request):
    return {"COOKIES": request.COOKIES}

# Add the 'ENVIRONMENT' setting to the template context
def environment(request):
    return {'ENVIRONMENT': settings.ENVIRONMENT}

