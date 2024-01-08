import os
from dotenv import load_dotenv
import random

# Load environment variables from .env file
load_dotenv()

class Data:
    base_url = os.getenv("BASE_URL")

    title = random.choice(["Mr", "Mrs"])

    countries = [
    "India",
    "United States",
    "Canada",
    "Australia",
    "Israel",
    "New Zealand",
    "Singapore"
    ]

    login_data_email = ""
    login_data_password = ""

    product_name = random.choice(["Jeans"])
