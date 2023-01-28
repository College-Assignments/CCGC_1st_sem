import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import urllib.request
import os
import json
import openai

"""
Email
1. Go to your Google Account settings.
2. Click on "Security"
3. Under "Signing in to Google," click on "App Passwords"
4. Select "Other (Custom Name)"
5. Enter a name for the application you are using to send email (e.g. "Python Script").
6. Click on "Generate"
7. The App Password will be displayed. Use this password in the script instead of your regular password.


1. go to https://beta.openai.com/account/api-keys > Top right corner > View API keys
2. Create new secret key
3. Copy the key to .env in this format OPENAI_API_KEY=sk-fxlzrsVQsoDs11tzlxxxxxxxxxxx
Reference: 
https://github.com/openai/openai-python
https://beta.openai.com/docs/api-reference/introduction
"""

def send_email(text):
    try:
        sender_email = os.getenv("SENDER_EMAIL")
        sender_password = os.getenv("SENDER_PASSWORD")
        receiver_email = os.getenv("RECEIVER_EMAIL")
    except:
        print("""please define SENDER_EMAIL, SENDER_PASSWORD, RECEIVER_EMAIL and OPENAI_API_KEY in ENV VAR e.g
                    please config your env:
                    SENDER_EMAIL=humbertechsociety@gmail.com
                    RECEIVER_EMAIL=humbertechsociety@gmail.com
                    SENDER_PASSWORD=xxx
                    OPENAI_API_KEY=xxx
                """ )

    message = """
    This is a test email sent using Python.
    Custom String can be added here: {text}""".format(text=text)
    msg = MIMEMultipart('alternative')
    msg["Subject"] = "Test Email in from a HTS workshop."
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg.attach(MIMEText(message))



    img_url = gen_openai_image()
    #img_url = "https://oaidalleapiprodscus.blob.core.windows.net/private/org-jIiuXhzxtaccKZE1ieQdyuqz/user-cATRqfFJfwo33siAra5ZZVU1/img-3u5sg4giWomjhTCI2kAv1Udw.png?st=2023-01-25T15%3A59%3A10Z&se=2023-01-25T17%3A59%3A10Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-01-25T15%3A49%3A35Z&ske=2023-01-26T15%3A49%3A35Z&sks=b&skv=2021-08-06&sig=sOFJqGziH6eyp/120VDPswhKa3t%2BNS%2BsvFiMM3o0lp0%3D"
    urllib.request.urlretrieve(img_url, "images/image.png")
    with open("images/image.png", 'rb') as f:
        img_data = f.read()
        image = MIMEImage(img_data, name='image.png')
        msg.attach(image)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email. {e}")
    finally:
        server.quit()

def history_tracker(user_data_path, email):
    target_field = 'calories'
    threshold = 150
    target_record = {}
    alert_bool = False
    with open(user_data_path, "r") as f:
        user_data = json.load(f)
        target_record = user_data[email]["food_consumed"]

    for timestamp, food_records in target_record.items():
        total_amount_per_timestamp = 0
        for food in food_records:
            if target_field in food:
                total_amount_per_timestamp+=food[target_field]

        if total_amount_per_timestamp > threshold:
            print("{} is exceeding the {} threshold({} at {})".format(email, target_field, threshold, str(timestamp)))
            alert_bool = True
    return alert_bool

def gen_openai_image():
    #openai.organization = ""
    openai.api_key = os.getenv("OPENAI_API_KEY")
    image_resp = openai.Image.create(prompt="an unhealthy guy in a hospital", n=1, size="512x512")
    print(image_resp)
    print(image_resp['data'][0]['url'])
    return image_resp['data'][0]['url']


            

    


    

    

