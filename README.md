# Django-Tutorial

## Requirements
- python > 3.5

## Installation
- Create a virtual environment for a project: 
```bash
  
  $ cd desktop/locallibrary/
  
  $ python -m venv venv

```

 ##### Virtualenv will isolate your Python/Django setup on a per-project basis.
- Start your virtual environment by running: 
```bash
    win :
    $ venv\Scripts\activate
    osx : 
    $ source\venv\bin\activate
```
- Generate pip requirements.txt:
```bash
    (optional)
    $ pip install --upgrade pip 
    $ pip install django~=1.10.0
    $ pip install django-toolbelt
    $ pip install dj-database-url gunicorn whitenoise
    $ pip freeze > requirements.txt  
```

- Installing requirements.txt:
```bash

    $ pip install -r requirements.txt

```


- git revise(optional):
```bash
    - remote list:  
        $ git remote -v
    - delete remote git : 
        $ git remote rm  'git_name'
```
## Usage