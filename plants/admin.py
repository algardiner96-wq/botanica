from django.contrib import admin
from .models import Plant, Symbolism, Variant


class VariantInline(admin.TabularInline):
    model = Variant
    extra = 1


@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ('name', 'scientific_name', 'plant_type', 'watering', 'sunlight')
    search_fields = ('name', 'scientific_name')
    list_filter = ('plant_type', 'watering', 'sunlight')
    inlines = [VariantInline]


admin.site.register(Symbolism)
admin.site.register(Variant)