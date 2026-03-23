import smtplib, random, pandas
import datetime as dt

bday_data = pandas.read_csv("birthdays.csv")
bday_list = bday_data.to_dict(orient="records")
now = dt.datetime.now()
user_name = "dineshathavantest1@gmail.com"
password = "phyligjhdrsiugsl"


for data in bday_list:
    wish_data = ""
    if data["day"] == now.day and data["month"] == now.month:
        with open(f"letter_templates/letter_{random.choice([1,2,3])}.txt") as file:
            letter_data = file.readlines()
            file.close()

        for line in letter_data:
            if "[NAME]" in line:
                replaced_line = line.replace("[NAME]", data["name"])
                wish_data += replaced_line
            else:
                wish_data += line

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=user_name, password=password)
            connection.sendmail(
                from_addr=user_name,
                to_addrs=data["email"],
                msg=f"Subject:Birthday wish\n\n{wish_data}"
            )
