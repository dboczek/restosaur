import re

RE_PARAMS = re.compile('(/:([a-zA-Z_]+))')


def to_url(urltemplate, params):
    uri = urltemplate

    params_to_replace = RE_PARAMS.findall(urltemplate)

    if params_to_replace:
        for needle, key in params_to_replace:
            try:
                uri = uri.replace(needle, '/%s' % params[key])
            except KeyError:
                pass
    return uri


def remove_parameters(urltemplate):
    uri = urltemplate

    params_to_replace = RE_PARAMS.findall(urltemplate)
    for needle, key in params_to_replace:
        uri = uri.replace(needle, '')
    return uri


def to_django_urlpattern(path):
    return RE_PARAMS.sub('/(?P<\\2>[^/]+)', path)


