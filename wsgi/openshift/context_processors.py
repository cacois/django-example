import django

def django_version(request):
    print django.VERSION
    return { 'django_version': django.VERSION }