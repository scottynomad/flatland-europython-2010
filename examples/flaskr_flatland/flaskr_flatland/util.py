
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
    error_filter.tags = ('input',)
    return error_filter

error_filter = error_filter_factory()

