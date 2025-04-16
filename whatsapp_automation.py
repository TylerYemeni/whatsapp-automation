import random
import time
import requests
from fake_useragent import UserAgent
from proxy_utils import get_random_proxy
from whatsapp_api import send_report
from account_utils import generate_fake_account
import logging

# إعدادات التسجيل
logging.basicConfig(filename="whatsapp_automation.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# إعداد وكيل المستخدم عشوائيًا
ua = UserAgent()

def get_random_user_agent():
    """توليد وكيل مستخدم عشوائي"""
    return ua.random

def send_report_with_rotation():
    """إرسال البلاغ مع تغيير الحسابات والبروكسيات بشكل دوري"""
    account = generate_fake_account()  # توليد حساب عشوائي
    proxy = get_random_proxy()  # اختيار بروكسي عشوائي
    user_agent = get_random_user_agent()  # اختيار وكيل مستخدم عشوائي

    # إعداد الجلسة مع البروكسي ووكيل المستخدم
    session = requests.Session()
    session.headers.update({"User-Agent": user_agent})
    session.proxies = {"http": proxy, "https": proxy}

    # تسجيل الدخول باستخدام الحساب الوهمي والبروكسيات
    whatsapp_session = rotate_account(account["username"], account["password"], session)

    if not whatsapp_session:
        logging.error(f"فشل تسجيل الدخول لحساب {account['username']}")
        return

    # تحديد نوع البلاغ
    report_content = "بلاغ ضد الحساب المشبوه"

    # إرسال البلاغ
    success = send_report(whatsapp_session, report_content)

    if success:
        logging.info(f"تم إرسال البلاغ بنجاح: {report_content}")
    else:
        logging.error(f"فشل إرسال البلاغ: {report_content}")

def main():
    """العمل بشكل مستمر على إرسال البلاغات"""
    while True:
        send_report_with_rotation()
        time.sleep(random.uniform(30, 90))  # تأخير عشوائي بين البلاغات

if __name__ == "__main__":
    main()
