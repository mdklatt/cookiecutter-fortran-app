{% set delim = "=" * cookiecutter.app_name|length %}
{{ delim }}
{{ cookiecutter.app_name }}
{{ delim }}

This is the {{ cookiecutter.app_name }} application.


Building
========

Application
-----------
.. code-block:: console

    $ mkdir build && cd build
    $ cmake -DCMAKE_BUILD_TYPE=Debug ../
    $ cmake --build .
    

Documentation
-------------
.. code-block:: console

    $ cd doc/doxygen
    $ doxygen Doxyfile
 
    
Running
=======

Application
-----------
.. code-block:: console

    $ cd build
    $ ./{{ cookiecutter.app_name }}
