=====
ex00
=====

ex00 is a simple Django app to upload and print to the srceen some files.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "ex00" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'ex00',
    ]

2. Include the ex00 URLconf in your project urls.py like this::

    url(r'^ex00/', include('ex00.urls')),

3. Run `python manage.py migrate` to create the ex00 models.

4. Visit http://127.0.0.1:8000/ex00/ to upload and visualize the files.