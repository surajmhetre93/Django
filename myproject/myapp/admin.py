from django.contrib import admin
from myapp.models import Login, Session, Student

# Register your models here.
admin.site.register(Login)
admin.site.register(Session)
admin.site.register(Student)