# Sphinx-Stylo

**It is extremely early stages for this extension. It is not likely to be robust**

Sphinx-Stylo is an extension to the [Sphinx](http://www.sphinx-doc.org/en/master/)
documentation tool that allows you to insert dynamically generated images created using
the [Stylo](https://alcarney.github.io/stylo) python library. Images can be defined
using the `.. stylo-image::` directive inline in your rst source files.

```rst
.. stylo-image::
   :align: center
   :img-width: 1920
   :img-height: 1080
   :display-width: 75%

   from stylo.color import FillColor
   from stylo.shape import Circle
   from stylo.image import SimpleImage

   color = FillColor("ffff00)
   circle = Circle(fill=True)

   image = SimpleImage(circle, color)
```

Then when a sphinx build is run your code will be executed and an image with the
given dimensions will be inserted into the final HTML page. 

If you want the code included alongside the inserted image then add the `:include-code:`
option to the list of options under the directive.

You **must** store your image in a variable called `image` for it to be picked up by the
extension.

## Getting Started

If you want to use this extension in your documentation then you first need to
install the extension using `pip`.

```sh
$ pip install sphinx-stylo
```

Then you need to add the extension to your `extensions = []` list in your project's `conf.py`

```py
extensions = [
    ...
    "sphinx_stylo"
]
```