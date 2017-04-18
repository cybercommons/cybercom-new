cyberCommons Platform documentation!
====================================

Using python tools as middleware, we demonstrate a loosely coupled service-orientated reference architecture for distributed computing workflows, implemented as a series of Docker contained services coupled together by a Python RESTful API. These containers in the reference architecture use MongoDB, RabbitMQ, Django RESTful and Celery to build a loosely coupled and scale-out tool stack. This reference stack can be used to manage data, register computational worker nodes with defined tasks and store process metadata on tasks that are run by the infrastructure. Computations can be scaled across a series of worker nodes on bare-metal or virtualized environments. This architecture stack serves as the reference environment used by The University of Oklahoma Libraries Informatics team to automate workflows for digital objects. This distribute processing of scientific research codes, both simple and complex, to command-line, web and mobile interfaces.

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

