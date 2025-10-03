from faker import Faker


fake = Faker('ru_RU')
fake_us = Faker('en_US')

print(fake.name())
print(fake.address())
print(fake.phone_number())
print(fake.email(),)
print(fake.passport_number())

data = {
    "name": fake.name(),
    "email": fake.email(),
    "age": fake.random_int(min=0, max=100),
    "password": fake.password(),
    "phone_number": fake_us.phone_number(),

}
print(data)


