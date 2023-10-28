from django.contrib import admin

# Register your models here.
from .models import UserModel, SocialMedia

admin.site.register(UserModel)
admin.site.register(SocialMedia)