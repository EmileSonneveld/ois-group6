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
	- lesion has no equivalent in OBO.
	- menorraghia contains a typo, we interpreted is as "menorrhagia"
	- nutritional_disorder has no equivalent OBO. Closest one is more brought, SYMP_0000473: "nutrition, metabolism, and development symptom"
	- weight_loss_or_gain has no equivalent OBO. Best would be to make this symptom obsolete, and propose 2 new symptoms: weight_loss and weight_gain
	- Some symptoms have multiple versions in the OBO, like 'intense x' of 'acute x'. We choose the most neutral version in those cases.
- Search for OBO ID's here: http://www.ontobee.org/search?ontology=SYMP&keywords=sweat&submit=Search+terms
	- Or here: http://www.ontobee.org/ontology/DOID?iri=http://purl.obolibrary.org/obo/DOID_10459

Postgresql should be running locally
Migrate from sqlite to other kind of database: https://gist.github.com/sirodoht/f598d14e9644e2d3909629a41e3522ad
python manage.py dumpdata > datadump.json

:: change settings.py to new database
python manage.py migrate --run-syncdb

python manage.py shell
from django.contrib.contenttypes.models import ContentType
ContentType.objects.all().delete()
quit()

python manage.py loaddata datadump.json