from datetime import datetime
import pandas
import random
import smtplib


MY_EMAIL = "YOUR_EMAIL@gmail.com"
MY_PASSWORD = "YOUR_PASSWORD"
recipient_email = "DESTINATION_EMAIL"


today = datetime.now()
today_tuple = (today.month, today.day)

print("Today's date:", today_tuple)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {
    (row["month"], row["day"]): row for (index, row) in data.iterrows()
}

print("Available birthdays:", birthdays_dict.keys())

if today_tuple in birthdays_dict:
    print("Birthday found for today!")
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    print("Email content prepared.")
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=recipient_email,
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
    print("Email sent!")
else:
    print("No birthdays today.")
