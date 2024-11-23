def project_name(request):
    from django.conf import settings
    return {'PROJECT_NAME': settings.PROJECT_NAME}
