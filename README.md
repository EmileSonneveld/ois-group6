# ois-group6

Python 3.7+

pip install gunicorn
pip install Pillow
pip install unidecode
pip install Django
python manage.py runserver 0.0.0.0:80

superuser: admin, admin
johny_doe, johny_doe

python manage.py makemigrations accounts
python manage.py migrate
python manage.py runserver

http://health.thendrie.be/accounts/git_pull/


Remake the database
===================
In case of the database got currupted due to a bad migration.
- Make an admin/superuser account
- Make Admin a doctor. It's ID should be 1
- Add the diseases/data following the examples in the PDF of deadline 2
- Note that when making adding a DoctorProfile to a User, it will becoma a staff member.
