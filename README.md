# Teacher_Directory

Setup
<hr>
The first thing to do is to clone the repository:

$ git clone https://github.com/jaseemrahman/Teacher_Directory
$ cd teacher_directory
Create a virtual environment to install dependencies in and activate it:

$ virtualenv2 --no-site-packages tenv
$ tenv/scripts/activate
Then install the dependencies:

(env)$ pip install -r requirements.txt
Note the (env) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by virtualenv2.

Once pip has finished downloading the dependencies:

(env)$ cd teacher_directory
(env)$ python manage.py runserver
And navigate to http://127.0.0.1:8000/.

Project Flow
<hr>
I am listed teacher list and profile button is able to show detail page. we have teacher bulk list importer option also.All user can able to do the importer option.

Tests
<hr>
To run the tests, cd into the directory where manage.py is:

(env)$ python manage.py test teacher_directory
