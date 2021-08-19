##################### Normal Starting Project ######################
import datetime as dt
import pandas
import random
import smtplib

BirthDate=dt.datetime.now()
today_month=BirthDate.month
today_day=BirthDate.day
Is_today_birthday=(today_month,today_day)

data=pandas.read_csv("birthdays.csv")


birthdays_dict = {(data_row["month"],data_row["day"]): (data_row["name"], data_row["email"]) for index, data_row in data.iterrows()}

UserId=input("Enter your email id: ")
UserPassword=input("Enter your password: ")

if Is_today_birthday in birthdays_dict:
    birthday_person=birthdays_dict[Is_today_birthday]
    
    file_path=f"letter_templates/letter_{random.randint(1,3)}.txt"

    with open(file_path) as letter_file:
        contents=letter_file.read()
        message=contents.replace("[NAME]",birthday_person[0])
        


    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=UserId,password=UserPassword)
        connection.sendmail(from_addr=UserId,to_addrs=birthday_person[1],msg=f"Subject:Happy Birthday\n\n{message}")
