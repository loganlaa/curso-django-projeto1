from django.contrib.auth.models import User  # Importando uma tabela de usuários
from django.db import models


# DEFINE A ESTRUTURA DOS DADOS QUE SERAO ARMAZENADOS NO SEU BANCO DE DADOS
# Cada Classe representa uma tabela no banco de dados
# Classe = Tabela
# Coluna = Atributo da classe
# SLUG e ID sao campos especiais porque sao indexados (podemos usar eles para buscar determinada receita)

class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):  # Método chamado quando você tenta chamar o model como uma string, já retorna o nome dela
        # automático. Aí não precisa ficar aparecendo object 1
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=65)  # é campo de input
    preparation_steps = models.TextField()  # é uma text área que nao tem limite de caaracter
    preparation_step_is_html = models.BooleanField(default=False)  # Por padrao, nao considera HTML, considera texto
    created_at = models.DateTimeField(auto_now_add=True)  # gera uma data no momento da criacao e nao mexe nela
    updated_ate = models.DateTimeField(auto_now=True)  # Gera a data apenas quando atualiza
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/')  # Salva a imagem em uma pasta por data (a foto
    # dá no media)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True  # Se alguem apagar a categoria, seta null para nao dar
        # inconssistencia na DB
    )
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True  # Se alguem apagar a categoria, seta null para nao dar
        # inconssistencia na DB
    )

    def __str__(self):
        return self.title

# EDITED
# title description slug
# preparantion_time preparation_time_unit
# Servings servings_unit
# preparation_steps
# preparation_step_is_html
# created_at updated_at
# is_published
# cover
# category (relacao)
# Author (relacao)
