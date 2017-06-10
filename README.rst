========
ShortURL
========

It's a simple web service with API for link shortening based on `Django <https://www.djangoproject.com/>`_.
An example of a deployed application: `ShortURL <https://shorturl.artcom-net.ru>`_.

----------
Installing
----------

.. code::

    $ git clone https://github.com/artcom-net/ShortURL
    $ cd ShortURL
    $ pip install -r requirements.txt

Change the parameters below in *settings.py*, if it's necessary:

.. code-block:: python

    # FQDN (host.example.com)
    HOSTNAME = 'localhost'

    PORT = '8000'

    # http(s)
    PROTOCOL = 'http'

    TITLE = 'ShortenerURL'

    SHORT_CODE_LENGTH = 6

---
API
---

~~~~~~~~~~~~~~~
Getting a Token
~~~~~~~~~~~~~~~

To obtain an access token, send a POST request to */api/auth/gettoken/* with parameters: *username*, *email*, *password*. Example:

.. code::

    $ curl --data "username=user_name&email=user@example.com&password=some_pass" http://your-django-host.com/api/auth/gettoken/

Response:

.. code::

    $ {"auth_token":"18ecd17306187da6ee2792fe3a919949b37175ce"}

~~~~~~~~~~~~~~~~~~~
Obtaining short URL
~~~~~~~~~~~~~~~~~~~

To get a short URL, send a POST request to */api/shorturl/*, pass the *url* parameter and add the *Authorization* header with the value
*"Token your_token"*. Example:

.. code::

    $ curl --data "url=http://host.example.com/long/path/" http://your-django-host.com/api/shorturl/ -H 'Authorization: Token 18ecd17306187da6ee2792fe3a919949b37175ce'

Response:

.. code::

    $ {"short_url":"http://your-django-host.com/87GP7Y/"}
