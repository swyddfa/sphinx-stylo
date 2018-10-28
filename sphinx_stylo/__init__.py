from ._version import __version__
from .directives import StyloImageDirective


def setup(app):

    app.add_directive("stylo-image", StyloImageDirective)

    return {"version": __version__}
