from django.contrib import admin
from .models import Category, Recipe


####### Há 2 MANEIRAS DE REGISTRAR UMA MODEL NA ADMIN
# Register your models here
# Se voce nao registrar, seus models nao vao aparecer na área administrativa para voce fazer um CRUD
# Configura a interface administrativa configurada automaticamente pelo framework

# Cria uma classe para a área administrativa do seu model (para adicionar na area admin)\


class CategoryAdmin(admin.ModelAdmin):
    ...


# Passa o model que a gente criou (Category) e a CategoryAdmin criada agora
# Ele vai registrar na área administrativa do site o Category através de CategoryAdmin
admin.site.register(Category, CategoryAdmin)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...

# Registra com esse decorator, passando só a model que será registrada
