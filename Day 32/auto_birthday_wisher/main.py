##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.

import random as r
import datetime as dt
import pandas
import smtplib

my_email = "mail@gmail.com"
my_pass = "dcwfzzmeswdxhdlm"
today = dt.datetime.today()

with open("birthdays.csv") as file:
    data = pandas.read_csv(file)
    data = data.to_dict("records")

for person in data:
    if person['month'] == today.month and person['day'] == today.day:
        # Choose random template
        template_file = "letter_templates/letter_" + str(r.randint(1,3)) + ".txt"
        with open(template_file) as file:
            letter = file.read()
        letter = letter.replace("[NAME]", person["name"])
        letter = letter.replace("Angela", "MyName")

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_pass)
            connection.sendmail(from_addr=my_email,
                                to_addrs="mail@gmail.com",
                                msg=f"Subject:Best wishes!\n\n{letter}")
