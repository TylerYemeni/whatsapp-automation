import random

def generate_fake_account():
    """توليد حساب واتساب وهمي"""
    username = f"fake_user{random.randint(1000, 9999)}"
    password = f"fake_pass{random.randint(1000, 9999)}"
    return {"username": username, "password": password}
