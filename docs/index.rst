About
=====

Sphinx-Stylo is an extension for the `Sphinx`_ documentation generator that allows you
to embed images created using `Stylo`_ directly into your documentation by writing the
code to generate them inline in your document.

.. stylo-image::
   :align: center
   :img-width: 1920
   :img-height: 1080
   :include-code:
   :display-width: 75%

   from stylo.shape import Circle
   from stylo.color import FillColor
   from stylo.image import SimpleImage

   circle = Circle(fill=True)
   color = FillColor("ff00ff")

   image = SimpleImage(circle, color)

.. toctree::
   :maxdepth: 2
   :caption: Index:

.. _Sphinx: http://www.sphinx-doc.org/en/master/index.html
.. _Stylo: https://alcarney.github.io/stylo/