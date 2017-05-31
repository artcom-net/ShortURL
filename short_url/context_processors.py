from django.conf import settings


TITLE = getattr(settings, 'TITLE', 'ShortenerURL')


def pass_title_processor(request):
    return {'title': TITLE}
