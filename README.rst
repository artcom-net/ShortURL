========
ShortURL
========

It's a simple web service for link shortening based on `Django <https://www.djangoproject.com/>`_.
An example of a deployed application: `ShortURL <https://shorturl.artcom-net.ru>`_.

----------
Installing
----------

.. code::

        $ git clone https://github.com/artcom-net/ShortURL
        $ cd ShortURL
        $ pip install -r requirements.txt

Change the parameters below in settings.py, if it's necessary:

.. code-block:: python

    # FQDN (host.example.com)
    HOSTNAME = 'localhost'

    PORT = '8000'

    # http(s)
    PROTOCOL = 'http'

    TITLE = 'ShortenerURL'

    SHORT_CODE_LENGTH = 6

