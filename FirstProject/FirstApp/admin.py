from django.contrib import admin
from FirstApp.models import Register
from FirstApp.models import SignUp
from FirstApp.models import Tour
from FirstApp.models import ModelFields
from import_export.admin import ImportExportModelAdmin

@admin.register(Register)
class ViewAdmin(ImportExportModelAdmin):
	pass

# Register your models here.
#admin.site.register(Register)
admin.site.register(SignUp)
admin.site.register(Tour)
admin.site.register(ModelFields)