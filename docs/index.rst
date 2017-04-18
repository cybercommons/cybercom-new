cyberCommons Framework!
=======================

The cyberCommons Framework is a loosely coupled service-orientated reference architecture for distributed computing workflows. The framework is implemented as a series of Docker contained services coupled together by a Python RESTful API. These containers in the reference architecture use MongoDB, RabbitMQ, Django RESTful and Celery to build a loosely coupled and horizontally scaleable software stack. This reference stack can be used to manage data, catalog metadata, register computational worker nodes with defined tasks. Computations can be scaled across a series of worker nodes on bare-metal or virtualized environments. This architecture stack serves as the reference environment used by The University of Oklahoma Libraries Informatics team to automate distributed workflows and catalog digital objects. This distribute processing of scientific research codes, both simple and complex, to command-line, web and mobile interfaces provides web-enabled automated workflows. 

.. image:: http://static.cybercommons.org/informatics/cybercommon_diagram.png

Contents:

.. toctree::
   :maxdepth: 2
   :numbered:

   installation
   configuration
   remote_worker
   rest_api
   permissions
   help
   authors


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

