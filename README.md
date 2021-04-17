![](https://miro.medium.com/max/3000/1*25Le7KoMK_z6BIaM8x74RA.png)
# <p align="center">TDB (The Django Boilerplate) </p>

We <img src="https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg" width="25px" height="15px"> Django!
It has been making our lives easier for so long, though it's a tedious job to write same the code every time we initialize a new Django project.

Hence, I've created this boilerplate for my future projects, it's using [Python 3.9](https://www.python.org/downloads/release/python-390/) and [Django 3.2 LTS](https://docs.djangoproject.com/en/3.2/) , so  it will be relevant for quite some time.

Things included in the boilerplate are as follow:
 - Docker & docker-compose files to kick-off development environment.
 - Commonly used Python packages bundled into Pipfile.lock
 - Pre-commit hooks integrated (run `pre-commit install` after installing all dependencies)
	 - Black
	 - iSort
	 - flake8
 - Ready to code folder structure of Django project with some base classes (i.e. BaseModel and BaseSerializer classes)
 - settings.py configured to read environment variables and jsonified configuration files, which is a better practice to manage sensitive data.

---------------------------------------------------------------------------------
PS: *This boilerplate is still under development, hence pinned versions of python packages might change, kindly modify accordingly before use.*
-------------------------------------------------------