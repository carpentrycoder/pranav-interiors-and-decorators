[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fexamples%2Ftree%2Fmain%2Fpython%2Fdjango&demo-title=Django%20%2B%20Vercel&demo-description=Use%20Django%204%20on%20Vercel%20with%20Serverless%20Functions%20using%20the%20Python%20Runtime.&demo-url=https%3A%2F%2Fdjango-template.vercel.app%2F&demo-image=https://assets.vercel.com/image/upload/v1669994241/random/django.png)

# Django + Vercel

This example shows how to use Django 4 on Vercel with Serverless Functions using the [Python Runtime](https://vercel.com/docs/concepts/functions/serverless-functions/runtimes/python).

## Demo
# Pranav Interior's Website

This project is the official website for Pranav Interiors, a dynamic and elegant interior design studio. The website is deployed using **Render** with cloud server storage, providing seamless performance and easy access.

![Pranav Interior's Logo](https://i.postimg.cc/sgbpMkLX/Black-Yellow-Thin-Interior-Design-Studio-Logo.png)

## Tech Stack

- **Django**: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **Python**: A powerful programming language used for server-side logic.
- **WSGI**: The Web Server Gateway Interface (WSGI) is used to communicate between the web server and the Django application.
- **PostgreSQL**: An open-source relational database used for storing and managing data.
- **Render**: A cloud platform used to deploy and host the website.
- **Cloud Server Storage**: To store static files and manage assets.

## Deployment Process

To deploy the Pranav Interior's website to Render, follow these steps:

1. **Set up the Django Project**: 
    - Create a virtual environment and install all necessary dependencies by running:
    ```bash
    pip install -r requirements.txt
    ```

2. **Set up PostgreSQL Database**: 
    - Create a PostgreSQL database and configure the `DATABASES` settings in Django's `settings.py` file.
    - Set up the necessary environment variables for the database connection, such as `DATABASE_URL` or `DATABASE_NAME`, `USER`, `PASSWORD`, and `HOST`.

3. **WSGI Setup**: 
    - Ensure that your WSGI file (`wsgi.py`) is correctly configured to interface with Render's cloud environment.

4. **Prepare for Deployment**:
    - Create a `Procfile` with the following contents:
    ```
    web: gunicorn your_project_name.wsgi:application
    ```
    - Install `gunicorn` for serving the app:
    ```bash
    pip install gunicorn
    ```

5. **Deploy to Render**:
    - Connect your project repository (on GitHub, GitLab, etc.) to Render.
    - Follow Render's steps to configure and deploy your Django app.
    - Make sure the static and media files are properly handled by the cloud storage on Render.

6. **Final Steps**:
    - Once deployed, visit the provided URL to confirm that your website is up and running.
    - Check logs in the Render dashboard for any errors during deployment.

## Features

- **Responsive Design**: The website adapts to different screen sizes for optimal user experience.
- **Dynamic Content**: Powered by Django templates and views to render dynamic content based on the user's needs.
- **Database Integration**: PostgreSQL manages all data related to user interactions and services.

## Conclusion

This project demonstrates how to build and deploy a Django application with PostgreSQL and a cloud server. It highlights modern practices in web development, cloud storage, and deployment with Render, ensuring that the Pranav Interior's website is scalable and reliable.

https://django-template.vercel.app/

## How it Works

Our Django application, `example` is configured as an installed application in `api/settings.py`:

```python
# api/settings.py
INSTALLED_APPS = [
    # ...
    'example',
]
```

We allow "\*.vercel.app" subdomains in `ALLOWED_HOSTS`, in addition to 127.0.0.1:

```python
# api/settings.py
ALLOWED_HOSTS = ['127.0.0.1', '.vercel.app']
```

The `wsgi` module must use a public variable named `app` to expose the WSGI application:

```python
# api/wsgi.py
app = get_wsgi_application()
```

The corresponding `WSGI_APPLICATION` setting is configured to use the `app` variable from the `api.wsgi` module:

```python
# api/settings.py
WSGI_APPLICATION = 'api.wsgi.app'
```

There is a single view which renders the current time in `example/views.py`:

```python
# example/views.py
from datetime import datetime

from django.http import HttpResponse


def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello from Vercel!</h1>
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)
```

This view is exposed a URL through `example/urls.py`:

```python
# example/urls.py
from django.urls import path

from example.views import index


urlpatterns = [
    path('', index),
]
```

Finally, it's made accessible to the Django server inside `api/urls.py`:

```python
# api/urls.py
from django.urls import path, include

urlpatterns = [
    ...
    path('', include('example.urls')),
]
```

This example uses the Web Server Gateway Interface (WSGI) with Django to enable handling requests on Vercel with Serverless Functions.

## Running Locally

```bash
python manage.py runserver
```

Your Django application is now available at `http://localhost:8000`.

## One-Click Deploy

Deploy the example using [Vercel](https://vercel.com?utm_source=github&utm_medium=readme&utm_campaign=vercel-examples):

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fexamples%2Ftree%2Fmain%2Fpython%2Fdjango&demo-title=Django%20%2B%20Vercel&demo-description=Use%20Django%204%20on%20Vercel%20with%20Serverless%20Functions%20using%20the%20Python%20Runtime.&demo-url=https%3A%2F%2Fdjango-template.vercel.app%2F&demo-image=https://assets.vercel.com/image/upload/v1669994241/random/django.png)
