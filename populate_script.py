import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
import django # noqa E402
django.setup()

from faker import Faker # noqa E402
from validate_docbr import CPF # noqa E402
import random # noqa E402
from clientes.models import Cliente # noqa E402


def criando_pessoas(quantidade_de_pessoas):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(quantidade_de_pessoas):
        cpf = CPF()
        nome = fake.name()
        email = '{}@{}'.format(nome.lower(), fake.free_email_domain())
        email = email.replace(' ', '')
        cpf = cpf.generate()
        rg = "{}{}{}{}".format(random.randrange(10, 99), random.randrange(100, 999), random.randrange(100, 999), random.randrange(0, 9) ) # noqa E501
        celular = "{} 9{}-{}".format(random.randrange(10, 21), random.randrange(4000, 9999), random.randrange(4000, 9999)) # noqa E501
        ativo = random.choice([True, False])
        p = Cliente(nome=nome, email=email, cpf=cpf, rg=rg, celular=celular, ativo=ativo) # noqa E501
        p.save()


criando_pessoas(50)
print('Sucesso!')
