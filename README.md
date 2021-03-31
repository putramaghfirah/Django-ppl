# Lab Django PPl

The clean, fast and right way to start a new Django `3.0` powered website.

## Getting Started

- Setup project environment with [virtualenv](https://pypi.org/project/pipenv/)
- Download and install [MongoDB](https://www.mongodb.com/download-center/community)

```bash
$ git clone https://github.com/putramaghfirah/Django-ppl.git
$ cd ppl
$ pipenv sync
$ pipenv shell
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```

## Features

* Basic Django scaffolding (commands, templatetags, statics, media files, etc).
* Split settings in two files. `settings_custom.py` for specific environment settings (localhost, production, etc). `projectname/settings.py` for core settings.
* Simple logging setup ready for production envs.

## Contributing

I love contributions, so please feel free to fix bugs, improve things, provide documentation. Just send a pull request.
