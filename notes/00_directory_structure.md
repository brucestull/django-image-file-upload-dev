# Project Directory Structure

* `tree /f /a`:  

    ```console
    PS C:\Users\FlynntKnapp\Programming\django-image-file-upload> tree /f /a .
    Folder PATH listing for volume Windows
    Volume serial number is 54A3-AA4E
    C:\USERS\FLYNNTKNAPP\PROGRAMMING\DJANGO-IMAGE-FILE-UPLOAD
    |   .gitignore
    |   db.sqlite3
    |   LICENSE
    |   manage.py
    |   Pipfile
    |   Pipfile.lock
    |   Procfile
    |   README.md
    |
    +---accounts
    |   |   admin.py
    |   |   apps.py
    |   |   forms.py
    |   |   models.py
    |   |   tests.py
    |   |   urls.py
    |   |   views.py
    |   |   __init__.py
    |   |
    |   \---migrations
    |           0001_initial.py
    |           __init__.py
    |
    +---config
    |   |   asgi.py
    |   |   urls.py
    |   |   wsgi.py
    |   |   __init__.py
    |   |
    |   \---settings
    |           common.py
    |           development.py
    |           production.py
    |
    +---notes
    |       00_commands_and_links.md
    |       00_directory_structure.md
    |
    \---templates
        |   base.html
        |   home.html
        |   staff.html
        |   user.html
        |
        \---registration
                login.html
                password_reset_complete.html
                password_reset_confirm.html
                password_reset_done.html
                password_reset_form.html
                signup.html
                update.html

    PS C:\Users\FlynntKnapp\Programming\django-image-file-upload>
    ```

## Repository Links

[README.md](../README.md)
