from string import Template

IMG = """
<img src="data:image/png;base64,$data" />
"""

IMG_WITH_STYLES = """
<img style="$styles" src="data:image/png;base64,$data" />
"""

IMG_WITH_CLASS = """
<img class="$classes" src="data:image/png;base64,$data" />
"""

IMG_WITH_STYLE_AND_CLASS = """
<img class="$classes" style="$styles" src="data:image/png;base64,$data" />
"""


def _render_image_with_styles(image_data, styles):

    template = Template(IMG_WITH_STYLES)
    return template.safe_substitute(data=image_data, styles=styles)


def _render_image_with_class(image_data, classes):

    template = Template(IMG_WITH_CLASS)
    return template.safe_substitute(data=image_data, classes=classes)


def _render_image_with_style_and_class(image_data, styles, classes):

    template = Template(IMG_WITH_STYLE_AND_CLASS)
    return template.safe_substitute(data=image_data, styles=styles, classes=classes)


def _get_alignment_class(align):
    alignments = {"center": "align-center"}

    return alignments[align]


def render_image(img_data, width=None, align=None):

    if width is not None and align is not None:
        styles = "width: {}".format(width)
        classes = _get_alignment_class(align)

        return _render_image_with_style_and_class(img_data, styles, classes)

    if width is not None:
        styles = "width: {}".format(width)
        return _render_image_with_styles(img_data, styles)

    if align is not None:
        classes = _get_alignment_class(align)
        return _render_image_with_class(img_data, classes)

    template = Template(IMG)
    return template.safe_substitute(data=img_data)
