![](https://miro.medium.com/max/3000/1*25Le7KoMK_z6BIaM8x74RA.png)
# <p align="center">TDB (The Django Boilerplate) </p>

We <img src="https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg" width="25px" height="15px"> Django!
Django has been making our lives easier for so long, though it's a tedious task to initialize and setup a Django project everytime.

Hence, I've created this boilerplate for my future projects, it's using [Python 3.10](https://www.python.org/downloads/release/python-3106/) and [Django 4.1](https://docs.djangoproject.com/en/4.1/releases/4.1/), so it will be relevant for quite some time.

Things included in the boilerplate are as follow:
 - Docker & docker-compose files to kick-off development environment.
 - Commonly used Python packages bundled into Pipfile.lock
 - Pre-commit hooks integrated (run `pre-commit install` after installing all dependencies)
	 - Black
	 - iSort
	 - flake8
 - Ready to code folder structure of Django project with some base classes (i.e. BaseModel and BaseSerializer classes)
 - settings.py configured to read environment variables and jsonified configuration files, which is a better practice to manage sensitive data.

[Update - 03/05/2021]
 - `sample` an example Django app initialized to explain, how to leverage this boilerplate.

[Update - 20/08/2022]
 - Python bumped upto version `3.10`
 - Django and DRF bumped upto version `4.1` and `3.13.1` respectively
 - `QuerySet.values` monkey-patched
 - `uuid` PK added in BaseModel
 - black bumped upto version `22.6.0`

[Update - 01/01/2024]
 - Python bumped upto version `3.11`
 - Django and DRF bumped upto version `4.2` and `3.14.0` respectively
 - `QuerySet.values` monkey-patch removed, as same can be achieved with `.only`
 - `.pre-commit-config.yaml` updated with latest versions to support Python 3.11
 - `python-decouple` integrated and deprecated custom `read_config` func

[Update - 17/06/2024]
 - Python bumped upto version `3.12`
 - PostgreSQL docker image bumped upto version `16.3`
	- Added support for `psycopg3`
 - Django and DRF bumped upto version `5.0` and `3.15.1` respectively
 - gunicorn bumped upto verion `22.0.0`
 - Default gunicorn worker class changed to `gthread`
 - Dockerfile and related compose files refactored
	- docker images changed to Debian from Alpine
	- large compose file split into smaller files and expected usage strategy is [merge](https://docs.docker.com/compose/multiple-compose-files/merge/)
		- Usage:
			`docker compose -f docker/compose/base.yml -f docker/compose/dev.yml up -d`

---------------------------------------------------------------------------------
PS: *This boilerplate is still under development, hence pinned versions of python packages might change, kindly modify accordingly before use.*
-------------------------------------------------------
