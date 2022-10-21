 
<!-- # django-singleton -->

- [The app](#the-app)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Usage](#usage)
- [The process of creating the app](#the-process-of-creating-the-app)
  - [setup a sensible environment](#setup-a-sensible-environment)
    - [pyenv](#pyenv)
    - [poetry](#poetry)
    - [Python Packages](#python-packages)
    - [VSCode](#vscode)
    - [tox](#tox)
    - [sphinx](#sphinx)
    - [documentation](#documentation)
    - [read the docs](#read-the-docs)
  - [project structure (part 1)](#project-structure-part-1)
  - [testing](#testing)
    - [pytest](#pytest)
    - [tox](#tox-1)
  - [documentation](#documentation-1)
  - [versioning](#versioning)
  - [package](#package)
  - [publish](#publish)

This is a silly little Django Reusable App which can be used purely as a guide for writing _other_ Django Resuable Apps.

Feel free to use the actual code - it *is* useful - but mostly this repository exists to document the process of creating, documenting, testing, and packaging a Django Reusable App.

## The app

A singleton is a class that can only be instanciated a single time.  `SingletonMixin` turns any Django Model into a singleton.  

### Installation

Install with pip.

```
pip install django-singleton
```

_or_

```
pip install -i https://test.pypi.org/simple/ django-singleton
```

Add _singleton_ to your _INSTALLED_APPS_

```
INSTALLED_APPS = [
  ...
  'singleton',
]
```

### Configuration

Update _settings.py_ if you feel like it.

```
SINGLETON_RAISE_ERROR_ON_SAVE = True|False
```

The default value is False.

### Usage


```
from django.db import models
from singleton.models import SingletonMixin

class MySingletonModel(SingletonMixin, models.Model):
  pass

my_singleton_instance = MySingletonModel.load()
```

Validation errors will ocurr if you try to save more than one instance of a singlton via a form (such as in the Django Admin).  These will be handled by normal Django form processing.  

If you try to save more than one instance of a singleton outside of a form then nothing will happen, unless `SINGLETON_RAISE_ERROR_ON_SAVE` is set to True in which case an exceptoin will be raised.

-----

## The process of creating the app


### setup a sensible environment

I do all of my coding on Ubuntu because I'm not insane.  

#### pyenv

I use pyenv to manage my python versions because I'm not insane.

To install pyenv first make sure the dependencies are installed:
```
$ sudo apt-get install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl
```

Then install pyenv itself:
```
$ curl https://pyenv.run | bash
```

and add the following to "~/.bashrc":
```
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

Reload the shell and install your favorite version of python; I'm using 3.10.0 at the time of writing.

#### poetry

Like most python developers, I started with pip and migrated to pipenv and toyed with piptools and embraced poetry.  Poetry handles virtual environments and package dependency management, building, publishing, etc.  To install it simply run:

```
curl -sSL https://install.python-poetry.org | python3 -
poetry self update
poetry completions bash >> ~/.bash_completion
```

Note that the resultant completions file doesn’t work in all versions of bash; multiword case statements have to be encased in quotes.

Next setup some config:

```
poetry config virtualenvs.in-project true`
```

This ensures that all virtual environments will be located in the project directory in a directory called ".venv".  This is very useful for integrating your virtual environments with your IDEs.

#### Python Packages

I have a standard set of python packages that I use for all of my projects.  I will mention them as needed throughout this guide, but for completeness sake, here is the full list:

* Django: obviously
* django-environ: lets me import variables either from the environment directory or from ".env" files
* django-appconf: classes for having app-specific configuration that can be overriden in the standard django settings module
* pytest & pytest-django & factory-boy: some tools to make testing a bit nicer
* tox: automates cross-version testing *and* helps w/ CI tasks
* yapf: yet another python formatter; makes my code pretty
* sphinx, sphinx-rtd-theme, myst-parser: automatic documentation
  
#### VSCode

An IDE makes life a lot easier.  I use VSCode.  I have therefore included a ".vscode/settings.json" file and a generic ".editorconfig" file to setup a few nice features like indentations and linting.  I do this for 2 reasons: **1)** It makes easier for *me* to code and **2)** it prevents (or, at least, makes it less likely) for *you* to push code that conflicts w/ my style.

My settings.json file works w/ the MS-Python plugin and specifies the python path to use (".venv" - the same location that poetry installs the virtual environment) and the linter to use (`.venv/bin/yapf`) as well as some personal style choices.
```
--style={dedent_closing_brackets: 1, split_all_top_level_comma_separated_values: 1}"
```

I _might_ revert to **black** instead of **yapf** simply because it can't be formatted and therefore it's impossible to get into arguments about what the code style should look like.  At the time of writing, though, there are just a few idiosyncracies about **black** that bug me.

I also have the particularly useful VSCode plugins installed:
* MS Python (this will install loads of other useful plugins)
* Markdown all in one
* Better commetns
* Better ToML
* DotENV
* Intellicode
* Tabnine

*Actually, I use a few more plugins for full-stack development, but these are the ones that are relevant for creating Django Resuable Apps.*

#### tox

Tox allows me to test my app across multiple library versions.  When writing Django Resuable Apps, the main libraries you care about are Python and Django, obviously.  If this were a more complex app, I might choose to test against multiple versions of other libraries.

#### sphinx

I use sphinx for documenting my code.  This will automatically parse docstings in code:

```
class MyClass(object):
  """
  I am a docstring for the class
  """

  def my_function(self, *args, **kwargs):
    """
    I am another docstring for the function
    """
    pass

  
  my_variable = True
  """
  I am yet another docstring for the variable
  (notice how I come after the definition)
  """
  
  pass
```

When I have comments that I don't need to be documented, I use the following syntax:

```
def my_complex_function(*args, **kwargs):
  for i in range(100):
    # this is a complex process that I want to leave a comment about, but I don't need sphinx to parse it
    do_something(i)
```



I'll talk about how to configure the documentation below.
I AM HERE

TODO:
* distributed tox (just use the -p flag)
* get tox to build documentation
* push documentation to readthedocs
* prevent tox from including docs dependencies for tests
* run tox on PRs
* https://pypi.org/project/tox-gh-actions/
* dynamic versioning: https://github.com/mtkennerly/poetry-dynamic-versioning
* badges

#### documentation

In a
#### read the docs

Next I want to see my documentation on readthedocs because I deserve it.  This requires signing up for an account on readthedocs.org via github.  

Then import your github project.  For some strange reason, readthedocs didn't recognise my repository and so I had to import it manually.  There is a very helpful GUI that walks you through the process.

In hindesight, using tox to build documentation is probably a bad idea b/c it pollutes the venvs w/ unused dependencies and I'm not really using it anyway since the integration between github and readthedocs will build it for me.

So, I'm just going to run `poetry shell && make html` in the docs directory whenever I want to see documentation locally.  And use a ".readthedocs.yml" to make sure that all my dependencies (such as django) are installed when readthedocs uses sphinx to build documentation.

So, readthedocs *can* parse the "pyproject.toml" file, but only top-level dependencies.  I therefore added some explicit dependencies for documenation using the "docs" dependency group: `poetry export -f requirments.txt --only docs --output docs/requirements.txt` and referenced it in the ".readthedocs.yml" like this:


```
python:
  install:
    - method: pip
      path: .
      extra_requirements:
        - docs/requirements.txt
```

I don't understand it either.

### project structure (part 1)

Some of the tools used to bootstrap a project create their own directory structure.  That can be a good thing.  But I want to wind up with my own custom directory structure.  So I am going to set that up by hand - with a little help with some templates I've prepared earlier.  I'll talk you through the setup process but most of the time you can just copy this repository and update the relavant bits of code.

First I need to create some empty directories for the project:

`mkdir -p django-singleton/singleton`
`mkdir -p django-singleton/example-project`
`cd django-singleton/`

If you want to use a specific python version for development, then run

`pyenv local 3.10.0`

Then use poetry to create a "pyproject.toml" file in the root directory and install a standard set of packages into the virtual environment (make sure you set the virtual environment to install in the project directory as above):

```
$ poetry init`
$ poetry add django django-environ django-appconf
$ poetry add --group dev tox pytest pytest-django factory-boy yapf
$ poetry add --group docs sphinx sphinx-rtd-theme myst-parser
```

Once this is done the `django-admin` command should be run to create the app directory and a project directory used for testing purposes.  The relationship between these two directories will become clearer below.

`django-admin startapp --template=https://github.com/allynt/django-reusable-app-template/archive/master.zip singleton` will populate the "singleton" directory with stubs to use to develop your app.  `django-admin startproject --template=https://github.com/allynt/django-reusable-app-project-template/archive/master.zip example example-project` will do the same thing for the "example-project" directory.

Once those directories are created make sure that the "singleton" app is included in the `INSTALLED_APPS` of "example-project/config/settings.py".  As you add more functionality to the app (such as adding a new view), you may have to update the project (such as including that new view in the project's URLs).

next setup sphinx documentation:

`sphinx-quickstart docs`

This will create a "docs folder w/ some initial configurations.  I like to add the following:



### testing

there are loads of ways to tweak pytest, I happen to be using pytest-django 
https://docs.pytest.org/en/7.2.x/reference/plugin_list.html

#### pytest 

#### tox

Tox allows me to test a matrix of package versions.  The obvious thing to do is to test it against different versions of Python & Django.  To speed things up you can run tox in parallel via `poetry run tox -p all` (although this doesn't provide as much output).

### documentation

I am using tox to generate documentation because *why not*?  I have added a separate section to the "tox.ini" file to deal w/ this.  Now, the [official tox documentation](https://tox.wiki/en/latest/example/documentation.html#sphinx) recommends bypassing the Makefile generated by `sphinx` but I disagree.  Why wouldn't I want to continue using the official approved way of generating documentation?  All I want to do w/ tox is to eventually integrate this into CI.  In order to build documentation run `poetry run tox -e docs`.  Note that I have tell `tox` about the "make" command by adding it to the "allowlist_externals" variable.
### versioning

### package 

### publish

use dev-py
