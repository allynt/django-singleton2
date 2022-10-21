sample RST file
====================

Here is a sample restructured text file.

I am *italics* and **bold** and `code`.

* I am a bulleted list
* I am the second line of a bulleted list

#. I am a numbered list
#. I am the second line of a numbered list

I am a code block...

.. code-block:: python

  from django.db import models
  from singleton2.models import SingletonMixin

  class MyModel(SingletonMixin, models.Model):
    pass
