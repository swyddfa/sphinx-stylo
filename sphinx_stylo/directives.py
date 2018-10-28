from docutils.nodes import raw, literal_block
from docutils.parsers.rst import Directive, directives
from sphinx.util.logging import logging

from .templates import render_image


logger = logging.getLogger(__name__)


class StyloImageDirective(Directive):
    """Allows users to insert an image generated with one of the stylo image classes."""

    option_spec = {
        "align": directives.unchanged,
        "img-height": directives.positive_int,
        "img-width": directives.positive_int,
        "include-code": directives.flag,
        "display-width": directives.unchanged,
    }

    # We need this to allow the users to type their code in.
    has_content = True

    def _get_img_options(self):

        # Setup the defaults.
        img_opts = {}

        if "display-width" in self.options.keys():
            img_opts["width"] = self.options["display-width"]

        if "align" in self.options.keys():
            img_opts["align"] = self.options["align"]

        return img_opts

    def _compile_code(self):
        """Extract the user's code from the directive and compile it ready for execution."""

        self.src = "\n".join(self.content)
        self.environment = {}
        self.code = compile(self.src, "<string>", "exec")

    def _get_img_data(self):
        """Run the user's compiled code and extract the image.
        
        Returns the rendered image as a base64 encoded string.
        """

        # Run the user's code to construct the image.
        exec(self.code, self.environment)

        width = self.options["img-width"]
        height = self.options["img-height"]
        image = self.environment["image"]

        return image(width, height, encode=True)

    def run(self):

        self._compile_code()

        image_data = self._get_img_data().decode("utf8")
        image_opts = self._get_img_options()

        html = render_image(image_data, **image_opts)
        nodelist = [raw("", html, format="html")]

        if "include-code" in self.options.keys():
            code_block = literal_block(self.src, self.src)
            code_block["language"] = "python"

            nodelist.append(code_block)

        return nodelist
