
AutoChromedriver
================

A helper library to automatically download chromedriver to current directory

Installation
------------

.. code-block::

   pip3 install --user autochromedriver

Usage
-----

Commandline
^^^^^^^^^^^

.. code-block:: bash

   autochromdriver [optional:version]

Library
^^^^^^^

.. code-block:: python

   import AutoChromedriver

   AutoChromedriver.download_chromedriver()

Documentation
-------------

.. code-block:: python

   def download_chromedriver(version="2.46")

Passing in a version is possible, and it defaults to ``2.46``.
