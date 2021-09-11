from main.forms.product_form import ProductForm
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from main import models, forms
# Register your models here.

class IndividualInstance(admin.StackedInline):
    model = models.Individual
    extra = 0

class EntityInstance(admin.StackedInline):
    model = models.Entity
    extra = 0

class UserAdmin(BaseUserAdmin):
    """отображает модель User в админ-панели."""
    list_display = ('username', 'balance', "is_active" ,'is_staff')
    list_filter = ('is_staff',"is_superuser")
    fieldsets = (
        (None, {'fields': ('password',)}),
        ('Personal info', {'fields': ('balance','is_active')}),
        ('Permissions', {'fields': ('is_staff','is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','password1',"password2","is_staff","is_active","is_superuser"),
        }),
    )
    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ()
    inlines = (IndividualInstance, EntityInstance)


class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    fieldsets = (
        ("Product info", {
            'fields': (
                'name',
                "specifications",
                "percent",
                "brokerage_commission",
                "exchange_commission",
                "due_date",
                "delivery_time",
                "processing_time",
            ),
        }),
        ("Add values", {
            "fields":(
                "date",
                "opening_val",
                "max_data_val",
                "min_data_val",
                "closing_val",
                "volume_val",
                "file_field"
            ),
        })
    )
    list_display = ["name"]


class EntityAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Entity._meta.fields]

class IndivAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Individual._meta.fields]

class DealAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Deal._meta.fields]

class TransactionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Transaction._meta.fields]

class NewsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.News._meta.fields]

class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.NewsCategory._meta.fields]

admin.site.register(models.User, UserAdmin)
admin.site.register(models.Entity, EntityAdmin)
admin.site.register(models.Individual, IndivAdmin)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Deal, DealAdmin)
admin.site.register(models.Transaction, TransactionAdmin)
admin.site.register(models.News, NewsAdmin)
admin.site.register(models.NewsCategory, NewsCategoryAdmin)