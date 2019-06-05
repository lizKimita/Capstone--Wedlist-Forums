from django.contrib import admin
from .models import Status,Posts,Profile, Solutions, Tips

# Register your models here.
admin.site.register(Status)
admin.site.register(Posts)
admin.site.register(Profile)
admin.site.register(Solutions)
admin.site.register(Tips)