# Django Picture File Upload - **APP IS COMPLETE : NEED TO CREATE DOCUMENTATION**

* Simple Django app which shows how to upload a file to a Django project.

## Interesting Concepts

### Resources

* [`<input type="file">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/file)
* [HTML attribute: `accept`](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/accept)
* Heroku:
  * [Configuring Django Apps for Heroku](https://devcenter.heroku.com/articles/django-app-configuration)
  * [Django and Static Assets](https://devcenter.heroku.com/articles/django-assets)
  * <https://github.com/heroku/python-getting-started>
* [Django File (and Image) Uploads Tutorial](https://learndjango.com/tutorials/django-file-and-image-uploads-tutorial)

### Production Deployment Options

* `SECRET_KEY`:

  ```python
  import os

  SECRET_KEY = os.environ.get(
    'DJANGO_SECRET_KEY',
    'cg#p$g+j9tax!#a3cup@1$8obt2_+&k3q+pmu)5%asj6yjpkag'
  )
  ```

* `DEBUG`:

  ```python
  import os

  DEBUG = os.environ.get('DJANGO_DEBUG', '') != 'False'
  ```

### Picture File Paths

* [`config/settings.py`](./config/settings.py):

  ```python
  MEDIA_ROOT = BASE_DIR / 'media-root'
  MEDIA_URL = '/media-url/'
  ```

  * [`pictures/models.py`](./pictures/models.py):
  
    ```python
    class Picture(models.Model):
        #...
        image = models.ImageField(upload_to='media/')
        #...
    ```
  
    * Database field:
      * `media/test_image_01.png`
    * Local directory:
      * `media-root\media\test_image_01.png`
    * Browser directory:
      * `media-url/media/test_image_01.png`
  
  * [`pictures/models.py`](./pictures/models.py):
  
    ```python
    class Picture(models.Model):
        #...
        image = models.ImageField(upload_to='images/')
        #...
    ```
  
    * Database field:
      * `images/test_image_01.png`
    * Local directory:
      * `media-root\images\test_image_01.png`
    * Browser directory:
      * `media-url/images/test_image_01.png`

### `MEDIA_ROOT`

* Open up config/settings.py in your text editor. We will add two new configurations. By default MEDIA_URL and MEDIA_ROOT are empty and not displayed so we need to configure them:

  * MEDIA_ROOT is the absolute filesystem path to the directory for user-uploaded files
  * MEDIA_URL is the URL we can use in our templates for the files
