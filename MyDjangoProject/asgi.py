"""
ASGI config for MyDjangoProject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

''' @gupta07ayush
WSGI stands for Web Server Gateway Interface, 
and ASGI stands for Asynchronous Server Gateway interface. 
They both specify the interface and sit in between the web server 
and a Python web application or framework.
One of their jobs is to handle incoming requests from the client.
 WSGI will process the requests sequentially, .
 it will carry out the instructions step-by-step, one after the other.
Remember that we process requests asynchronously. 
So requests don’t have to wait on the others before it to finish.
'''


import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyDjangoProject.settings')

application = get_asgi_application()
