# Flask-Starter

This is an easy to use broilerplate to get productive with flask right away.


## Setup Guide:
  * You should have these installed:
      * python 3.5.x - Use official python installer (https://www.python.org/downloads/release/python-353/)
      * pip  `sudo easy_install pip`
      * tox  `pip install tox`

  * **Project setup**
      * `./setup.sh` to setup the python virtual environment - put all setup steps here
      * To build docs - `source activate && cd docs && make html && cd ..`
      * Make sure your virtual environment is activated while you are developing on this project

  * **Development**
      * Activate virtual environment `source activate`
      * Run server `python manage.py runserver` or live reload with `python manage.py runserver`
      * You can also just do `cd flask_app && python __init__.py` if you don't want gunicorn

  * **Dependencies:**
    * Python dependencies are specified in requirements.txt
    * Whenever a new package is added to requirements.txt, please add package over there with description.

## Documentation
  * Documentation is rebuilt on readthedocs.org whenever a commit is pushed to this repository.
  * You would need to create an account on readthedocs.org and add service to your github account to have the same functionality.


## Development Guide:

   * **Manage.py CLI**
       * Provides you with following commands:
           * runserver -  To run the development server with config defined in config.py
           * gunicorn -  To run multiple instances of the server for scalability
           * dirs - To list important directories configured in main app
           * config - To print out app config
           * routes - To list routes configured in an app
           * **Auto-Restart of server on code change:**
             * It's convenient to have server reload modified code automatically.
             * For that, you can run server in debug mode:
                ```
                python manager.py runserver -r
                ```
   * **Directories**
       * All web application projects tend to have at least the following directories:
           * templates - To keep html templates
           * static - This directory has subdirectories - js, img and css to keep static content.
           * uploads - Temporary place to hold uploads from user
