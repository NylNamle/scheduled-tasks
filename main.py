# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.

from datetime import datetime
import pandas as pd
import smtplib
import os

# import os and use it to get the Github repository secrets
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

now = datetime.now()
today = (now.month,now.day)

data = pd.read_csv("birthdays.csv")
birthdays = {(row["month"], row["day"]): row.to_dict()
    for _, row in data.iterrows()}
if today in birthdays:
    person = birthdays.get(today)
    print(person["name"])
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)

        if person["name"] == "Self":
            with open("letter_templates/letter_1.txt", "r", encoding="utf-8") as f:
                body = f.read()
            msg = f"Subject: Happy Birthday!!\n\n{body}"
        elif person["name"] == "Bear":
            with open("letter_templates/letter_2.txt", "r", encoding="utf-8") as f:
                body = f.read()
            msg = f"Subject: Happy Birthday!!\n\n{body}"

        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=person["email"],
            msg=msg.encode("utf-8")
        )
