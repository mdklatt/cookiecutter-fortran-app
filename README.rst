====================================
Fortran Application Project Template
====================================
.. |travis.png| image:: https://travis-ci.org/mdklatt/cookiecutter-fortran-app.png?branch=master
   :alt: Travis CI build status
   :target: `travis`_
.. _travis: https://travis-ci.org/mdklatt/cookiecutter-fortran-app
.. _Cookiecutter: http://cookiecutter.readthedocs.org

|travis.png|

This is a `Cookiecutter`_ template for creating a Fortran application project.


Template Project Features
=========================
.. _Cmake: https://cmake.org 
.. _Doxygen: http://www.stack.nl/~dimitri/doxygen
.. _MIT License: http://choosealicense.com/licenses/mit

* `CMake`_ builds
* `Doxygen`_ documentation
* `MIT License`_


Template Application Features
=============================
* CLI with subcommands
* Logging (coming soon)


Usage
=====
Install Python requirements for using the template:

.. code-block:: console

    $ pip install --requirement=requirements.txt --user 


.. _GitHub: https://github.com/mdklatt/cookiecutter-fortran-app

Create a new project directly from the template on `GitHub`_:

.. code-block:: console
   
    $ cookiecutter gh:mdklatt/cookiecutter-fortran-app
