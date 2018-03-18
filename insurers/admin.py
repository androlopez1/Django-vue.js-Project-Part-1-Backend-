from django.contrib import admin

from .models import RiskType, RiskField


class RiskFieldInline(admin.TabularInline):
    model = RiskField
    extra = 2
    
class RiskTypeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['risk_name']}),
        ('Date information', {'fields': ['pub_date'], 'classes':['collapse']}),
        ]
    inlines = [RiskFieldInline]
    list_display = ('risk_name','pub_date')
    list_filter = ['pub_date']
    search_fields = ['risk_name']
    

admin.site.register(RiskType, RiskTypeAdmin)

