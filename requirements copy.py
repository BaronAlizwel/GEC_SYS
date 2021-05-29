Multiple models in a View Class


class IndexView(generic.ListView):
    template_name = 'character/index.html'
    context_object_name = 'character_series_list'

    def get_queryset(self):
        return CharacterSeries.objects.order_by('name')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['character_universe_list'] = CharacterUniverse.objects.order_by(
            'name')
        return context


***************************************************************************************************************


Django Models - Field Relationships
Sometimes business logic require relationships among attributes of different model classes. Their are three field relationships in django models: ForeignKey(), OneToOneField() and ManyToManyField().

Django ForeignKey
ForeignKey is like a many-to-one relationship. It requires two positional arguments namely Classname and on_delete.
Classname is the class to which model is related.
on_delete = models.CASCADE means when the Super class object is deleted all its reflections as ForeignKey also gets deleted. For example when the Customer object in below model is deleted it's related Order objects are also deleted.

   class Customer(models.Model):
        name = models.CharField(max_length=30)

        def __str__(self):
            return self.name

    class Order(models.Model):
        customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
        order_details = models.TextField()

Django OneToOneField
OneToOneField is very similar to ForeignKey except the realtionship is like unique =True.
For example, if one Person can be have only one nationality it can described as below:

    class Person(models.Model):
        name = models.CharField(max_length=30)

        def __str__(self):
            return self.name

    class Citizenship(models.Model):
        person = models.OneToOneKey(Person, on_delete=models.CASCADE)
        country = models.CharField(max_length=30)

Django ManyToManyField
A many-to-many relationship requires only one argument i.e, the class to which the model is related. It can be understood with the example below:

    class Person(models.Model):
        name = models.CharField(max_length=30)

    class Group(models.Model):
        name = models.CharField(max_length=128)
        members = models.ManyToManyField(
            Person,
            through='Membership',
            through_fields=('group', 'person'),
        )

    class Membership(models.Model):
        group = models.ForeignKey(Group, on_delete=models.CASCADE)
        person = models.ForeignKey(Person, on_delete=models.CASCADE)
        inviter = models.ForeignKey(
            Person,
            on_delete=models.CASCADE,
            related_name="membership_invites",
        )
        invite_reason = models.CharField(max_length=64)

Use MySQL as Database Engine
    Step 1: Download MySQL from usi .msi file. Select 'Server only' when prompted
    https: //dev.mysql.com/downloads/installer/

    Step 2: Install python mysql client
    pip install pymysql

    Step 3: Under __init__.py mention
    import pymysql
    pymysql.install_as_MySQLdb()

    Step 3: Select database engine under settings
    DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': 3306,
    }
    }

    Note: Replace query = query.decode(errors='replace') with query = errors ='replace' in operations.py if required.

Use PostgreSQL as Database Engine
    Step 1: Download postgresql from
    https: //www.enterprisedb.com/downloads/postgres-postgresql-downloads

    Step 2: Install python postgresql client
    pip install psycopg2

    Step 3: Select database engine under settings
    DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': 5432,
    }
    }

Link: https://www.programink.com/django-tutorial/django-models.html


*******************************************************************************************************************************
