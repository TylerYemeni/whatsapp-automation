import requests

def rotate_account(username, password, session):
    """تسجيل الدخول باستخدام الحساب المحدد والبروكسي"""
    login_url = "https://api.whatsapp.com/login"
    credentials = {"username": username, "password": password}
    try:
        response = session.post(login_url, data=credentials)
        if response.status_code == 200:
            return session
        else:
            return None
    except Exception as e:
        print(f"فشل تسجيل الدخول: {e}")
        return None

def send_report(session, report_content):
    """إرسال البلاغ باستخدام الحساب والبروكسي المحدد"""
    report_url = "https://api.whatsapp.com/send_report"
    data = {"content": report_content}
    try:
        response = session.post(report_url, data=data)
        return response.status_code == 200  # التأكد من إرسال البلاغ بنجاح
    except requests.RequestException as e:
        print(f"فشل في إرسال البلاغ: {e}")
        return False
