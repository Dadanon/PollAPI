Hello! Here you will see the magic of Django and DRF. You can see question list,

a detailed question with variants to vote, you may even go voting whatever you like!

**There are main API endpoints:**

`127.0.0.1:8000/api/` - a root endpoint, doesn't show anything but from here

everything starts.

`127.0.0.1:8000/api/questions` - you can see question list with all the info

except choices

`127.0.0.1:8000/api/questions/1/` - this is the URL for e.g. 1st question.

You can change 1 to any available number. Here are the choices yet.

`127.0.0.1:8000/api/choices/` - and here you can see choices list.

With id's and number of votes.

`127.0.0.1:8000/api/questions/1/vote/` - and finally you can vote for any question

(e.g. 1st as in the URL, just replace 1 by anything).

With all this functionality you can also send POST, PATCH, DELETE requests with

information in JSON format. Try and enjoy!

**--------------------------------------------------------
--------------------------------------------------------**

Here is the instruction how to run this project on your computer:

In the console go to the folder you want and type:

**`git clone https://github.com/Dadanon/pollapi.git`**

Go to the project directory, enter to the virtual environment by

typing **`pipenv shell`** (if you have not **`pipenv`** - type **`pip install pipenv`** then install packages with the command

******`pipenv install`******, make migrations with

**`python manage.py migrate`** and run - **`python manage.py runserver`** !



