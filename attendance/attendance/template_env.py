from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage
from django.utils import translation
from jinja2 import Environment


def environment(**options):
    if 'extensions' not in options:
        options['extensions'] = []

    options['extensions'].append('jinja2.ext.loopcontrols')
    options['extensions'].append('jinja2.ext.i18n')
    options['extensions'].append('jinja2.ext.do')

    env = Environment(**options)
    env.install_gettext_translations(translation)

    env.globals.update({

    })

    env.globals['static'] = static_without_cache
    env.globals['BASE_URL'] = settings.BASE_URL

    return env


def static_without_cache(name):
    path = staticfiles_storage.url(name)
    return path