from faker import Faker

fake = Faker()

class RandomData:
    def generate_fake_name():
        return fake.name_nonbinary()
    
    def generate_fake_first_name():
        return fake.first_name_nonbinary()
    
    def generate_fake_last_name():
        return fake.last_name_nonbinary()

    def generate_fake_email():
        return fake.ascii_safe_email()

    def generate_fake_password(length):
        return fake.password(length)
    
    def generate_fake_phone_number():
        return fake.phone_number()
    
    def generate_fake_company():
        return fake.company()
    
    def generate_fake_address():
        return fake.address()
    
    def generate_fake_state():
        return fake.state()
    
    def generate_fake_city():
        return fake.city()
    
    def generate_fake_name():
        return fake.name_nonbinary()
    
    def generate_fake_postcode():
        return fake.postcode()
    
    def generate_fake_subject():
        return fake.text(max_nb_chars=20)
    
    def generate_fake_message():
        return fake.paragraph(nb_sentences=3)
    
    def generate_fake_invalid_first_name():
        return str(fake.random_number(digits=4))

    def generate_fake_invalid_last_name():
        return str(fake.random_number(digits=4))

    def generate_fake_invalid_username():
        return str(fake.random_number(digits=4))

    def generate_fake_invalid_email():
        return f"{fake.last_name()}@{fake.domain_name()}"

    def generate_fake_invalid_password():
        return str(fake.random_number(digits=4))

    def generate_fake_invalid_phone_number():
        return str(fake.random_number(digits=4))