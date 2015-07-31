# django-model-validation-problem
django.db.models.Model full_clean() problem when set Meta class abstract to True and you have a unique field in abstract model class, it will check uniqueness in the database, but this model do not have a mapping table, it will throw exception

# how to run the project and see the error

* firstly, run the server using command, make sure your 8000 port is not used
	
	$python manage.py runserver

* secondly, access the url "localhost:8000/validate/" using browser or other tool which can send http request

* thirdly, you can see exception error on the server running console

