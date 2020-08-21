import requests
from pprint import pprint

import smtplib
import os
from email.message import EmailMessage


email_address = os.environ.get('email_address')
email_pwd = os.environ.get('python_passwd')
contacts = ['juliovarens@nauta.cu','h4bibfigueredo@gmail.com']

def weather_data(query):
    res=requests.get('http://api.openweathermap.org/data/2.5/weather?'+query+'&APPID=841d2094f454df182667d740afee7a4d&units=metric');
    return res.json();

def print_weather(result, city):
    pw = ""
    pw = "{} Temperatura: {}°C ".format(city,result['main']['temp']) + "\n"
    pw = pw + "Velocidad del Viento: {} m/s".format(result['wind']['speed'])+"\n"
    #pw = pw + "D: {}".format(result['weather'][0]['description']) + "\n"
    pw= pw + "Tiempo generalmente: {}".format(result['weather'][0]['main']) + "\n"
    return (pw)
# deather = ''

def main():
    city='Cienfuegos'
    query ='q='+city
    w_data = weather_data(query)
    pr = ""
    pr = print_weather(w_data,city)

    # send_email():
    msg = EmailMessage()
    msg['Subject'] = "Estado del tiempo en Cienfuegos, Cuba"
    msg['From'] = email_address
    msg['To'] = contacts
     #send email to multiple contacts, see contacts declare above
     #msg['To'] = contacts

    msg.set_content(pr)

        #msg.attach(MIMEText(results49,'plain'))
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_address, email_pwd)
        smtp.send_message(msg)

if __name__=='__main__':
    main()

#this is just another test
#testing this file with a different fork mate, hfigueredoluis


