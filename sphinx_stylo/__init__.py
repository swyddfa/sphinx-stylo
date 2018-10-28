from sphinx.util import logging

from ._version import __version__
from .directives import StyloImageDirective

logger = logging.getLogger(__name__)


def setup(app):

    logger.info("Registering sphinx-stylo extension.")
    app.add_directive("stylo-image", StyloImageDirective)

    return {"version": __version__}
