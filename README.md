# ois-group6

Python 3.7+

pip install gunicorn
pip install Pillow
pip install unidecode
pip install Django
pip install psycop2
python manage.py runserver 0.0.0.0:80

superuser: admin, admin
johny_doe, johny_doe

python manage.py makemigrations ois_app
python manage.py migrate
python manage.py runserver

http://health.thendrie.be/accounts/git_pull/


Remake the database
===================
In case of the database got currupted due to a bad migration.
- Make an admin/superuser account
- Make Admin a doctor. It's ID should be 1
- Add the diseases/data following the examples in the PDF of deadline 2
- For completeness: Add the symptoms from the slides

Postgresql should be running locally
Migrate from sqlite to other kind of database: https://gist.github.com/sirodoht/f598d14e9644e2d3909629a41e3522ad
