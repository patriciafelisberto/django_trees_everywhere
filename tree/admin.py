from django.contrib import admin

from tree.models import(
    Account,
    PlantedTree,
    Profile,
    Tree,
)


class PlantedTreeInline(admin.TabularInline): 
    model = PlantedTree
    can_delete = False  
    extra = 0  
    max_num = 0  
    readonly_fields = ('user', 'location', 'age', 'planted_at', 'account')  


class TreeAdmin(admin.ModelAdmin):
    list_display = ('name', 'scientific_name')
    inlines = [PlantedTreeInline]


class PlantedTreeAdmin(admin.ModelAdmin):
    list_display = ('tree', 'user', 'location', 'age', 'planted_at', 'account')


admin.site.register(Account)
admin.site.register(PlantedTree, PlantedTreeAdmin)
admin.site.register(Profile)
admin.site.register(Tree, TreeAdmin)
