
def error_filter_factory(class_='error'):
    """Returns an HTML generation filter annotating field CSS class on error.

    :param class: The css class to apply in case of validation error on a
                  field.  Default: 'error'
    """
    def error_filter(tagname, attributes, contents, context, bind):
        if bind is not None and bind.errors:
            current_css_classes = attributes.get('class', '').split()
            attributes['class'] = ' '.join(current_css_classes + [class_])
        return contents
    error_filter.tags = ('input',)
    return error_filter

error_filter = error_filter_factory()

