About
=====

Sphinx-Stylo is an extension for the `Sphinx`_ documentation generator that allows you
to embed images created using `Stylo`_ directly into your documentation by writing the
code to generate them inline in your document.

.. <image>

.. stylo-image::
   :align: center
   :img-width: 1920
   :img-height: 1080
   :display-width: 75%

   from stylo.shape import Circle
   from stylo.color import FillColor
   from stylo.image import SimpleImage

   circle = Circle(fill=True)
   color = FillColor("ff00ff")

   image = SimpleImage(circle, color)

.. </image>

The image above was generated using the following snippet of reStructuredText

.. literalinclude:: index.rst 
   :start-after: .. <image>
   :end-before: .. </image>

If you want to include the code alongside the image then you can use the
:code:`:include-code:` option.


.. <image-code>

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

.. </image-code>



.. literalinclude:: index.rst 
   :start-after: .. <image-code>
   :end-before: .. </image-code>


Getting Started
---------------

.. note::

   This is extension is barely more than a proof of concept at this stage. It will
   not be very robust.

If you want to use this extension in your own sphinx project you first need to
install it using pip

.. code-block:: sh

   $ pip install sphinx-stylo

Then enable the extension by adding it to your :code:`extensions = []` list in your
project's :code:`conf.py`

.. code-block:: python

   extensions = [
       ...
       "sphinx_stylo"
   ]

This will make the :code:`.. stylo-image::` directive available for use in your rst
source files.

.. important::

   You *must* assign the image you want rendered to a variable called :code:`image`
   for it to be picked up by the extension.

.. toctree::
   :maxdepth: 2
   :caption: Index:

.. _Sphinx: http://www.sphinx-doc.org/en/master/index.html
.. _Stylo: https://alcarney.github.io/stylo/