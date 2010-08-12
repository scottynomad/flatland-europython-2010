from flatland import Unspecified


class AttributeDict(dict):
    """Dict exposing keys as instance properties.

    For demonstrating Form.from_object and Form.update_object
    """

    def __getattr__(self, key, default=Unspecified):
        if key in self:
            return self[key]
        up = super(AttributeDict, self).__getattr__
        if default is Unspecified:
            return up(key)
        else:
            return up(key, default)

    def __setattr__(self, key, value):
        if key not in self:
            raise AttributeError()
        self['key'] = value


def error_filter_factory(class_='error'):
    """Returns an HTML generation filter annotating field CSS class on error.

    :param class: The css class to apply in case of validation error on a
                  field.  Default: 'error'
    """
    def error_filter(tagname, attributes, contents, context, bind):
        if bind is not None and bind.errors:
            if 'class' in attributes:
                attributes['class'] = ' '.join(attributes['class'], class_)
            else:
                attributes['class'] = class_
        return contents
    return error_filter


class AttributeCSSClassFilter(object):
    """Markup generation filter.

    :param class: CSS class to append when *predicate* is True.

    :param tags: Tags types the filter applies to (e.g. (input, textarea).

    :param predicate: One-argument callable that decides whether or not
                      the filter gets applied.
                      Default: bool(element.errors)

    """

    @classmethod
    def _has_error(cls, bind):
        return bind.errors

    def __init__(self, class_='error', tags=None, predicate=None):
        self.class_ = class_
        self.tags = tags
        self.predicate = predicate or AttributeCSSClassFilter._has_error

    def __call__(self, tagname, attributes, contents, context, bind):
        if bind is not None and self.predicate(bind):
            if 'class' in attributes:
                attributes['class'] = ' '.join(attributes['class'], self.class_)
            else:
                attributes['class'] = self.class_
        return contents


