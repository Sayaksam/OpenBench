from django.contrib import admin
from OpenBench.models import LogEvent, Engine, Profile, Machine, Result, Test

admin.site.register(LogEvent)
admin.site.register(Engine)
admin.site.register(Profile)
admin.site.register(Machine)
admin.site.register(Result)
admin.site.register(Test)
