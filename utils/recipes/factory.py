#from inspect import signature
from random import randint
from faker import Faker

def rand_ratio():
    return randint(840, 900), randint(473, 573)

fake = Faker('pt_BR') # Cria uma instância do Faker configurada para gerar dados no formato brasileiro (pt_BR)
# print(signature(fake.random_number))

def make_recipe():
    return {
        'id': fake.random_number(digits=2, fix_len=True),
        'title': fake.sentence(nb_words=6),
        'description': fake.sentence(nb_words=12),
        'preparation_time': fake.random_number(digits=2, fix_len=True),
        'preparation_time_unit': 'Minutos',
        'servings': fake.random_number(digits=2, fix_len=True),
        'serving_unit': 'Porções', 
        'preparation_steps': fake.text(3000), 
        'created_at': fake.date_time(),
        'author': {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
        },
        'category': {
            'name' : fake.word()
        },
        'cover': {
            'url': 'https://loremflickr.com/%s/%s/food,cook' % rand_ratio(), #Um dicionário com a URL de uma imagem aleatória, usando as dimensões geradas pela função rand_ratio.
        } 
    }
    
if __name__ == '__main__':
    from pprint import pprint #pprint é usada para imprimir estruturas de dados de forma mais legível e organizada.
    pprint(make_recipe()) #Usa pprint para imprimir o dicionário retornado pela função make_recipe() de forma legível.
    # abreviação de “pretty-print”).