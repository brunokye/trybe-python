from faker import Faker


faker = Faker(locale='pt_BR')

Faker.seed(0)

print(faker.name())
print(faker.cpf())
print(faker.email())
print(faker.password())
