from faker import Faker

def generate_new_user_data():
    fake = Faker("en_US")

    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "username": fake.user_name(),
        "email": fake.email(),
        "password": fake.password(length=12)
    }
