# django-model-validation-problem
django.db.models.Model full_clean() problem when set Meta class abstract to True when you have a unique field in abstract model class, it will check uniqueness in the database, but this model do not have a mapping table, it will throw exception
