import requests
import smtplib
import os
from dotenv import load_dotenv
    

response=requests.get(url="http://api.open-notify.org/iss-now.json")


my_lat=22.572645,
my_long=88.363892,
#print(response.status_code)
#response codes meanings:
#1XX    Means that you need to wait
#2XX    Means that you what you searched for is there for you.
#3XX    Means that you have no permission for the accessing the webpage.
#4XX    Means that you(the user) screwed up.
#5XX    Means that i(the server) screwed up.
response.raise_for_status()
data=response.json()
# print(data)
latitude=float(data["iss_position"]["latitude"])
longitude=float(data["iss_position"]["longitude"])
print(type(latitude))
# print(f"The latitude is {latitude} and the longitude is {longitude}")
while True:
    if latitude-5<=my_lat<=latitude+5 and longitude-5<=my_long<=longitude+5 :
        connection=smtplib.SMTP(os.getenv("SMTP_ADDRESS"),port=587)
        connection.starttls()
        connection.login(user=os.getenv("SENDER_EMAIL"),password=os.getenv("PASSWORD"))
        connection.sendmail(from_addr=os.getenv("SENDER_EMAIL"),
                                to_addrs=os.getenv("RECEIVER_EMAIL"),
                                msg=f"Subject:International Space Station Update!!\n\nCurrently The International Space Station(ISS) is zooming right over your hometown of Kolkata!\nHave a wonderful day ahead!\n\n~Soumyadeep Dey ;-)"
                                )
        connection.close()
