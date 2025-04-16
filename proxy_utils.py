import random

def get_random_proxy():
    """إحضار بروكسي عشوائي من ملف البروكسيات"""
    try:
        with open("proxies.txt", "r") as file:
            proxies = file.readlines()
            return random.choice(proxies).strip()  # اختر بروكسي عشوائي
    except FileNotFoundError:
        raise Exception("ملف البروكسيات 'proxies.txt' غير موجود!")
