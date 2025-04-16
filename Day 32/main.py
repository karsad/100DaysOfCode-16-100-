import smtplib
import datetime as dt
import random as r

my_email = "mail@gmail.com"
my_pass = "dcwfzzmeswdxhdlm"

now = dt.datetime.now()
if now.weekday() == 2:
    with open("quotes.txt") as file:
        data = file.readlines()
    quote = r.choice(data)
    print("Sending email with:", quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_pass)
        connection.sendmail(from_addr=my_email,
                            to_addrs="mail@gmail.com",
                            msg=f"Subject:Greetings on Wednesday!\n\nThis is a sentence for you today:\n{quote}")