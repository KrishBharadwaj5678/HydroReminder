import streamlit as st
import time
from plyer import notification

st.set_page_config(
    page_title="HydroReminder",
    page_icon="water.ico",
    menu_items={
        "About":"""HydroReminder is designed to simplify your hydration journey. We understand the challenges of staying hydrated throughout the day, which is why we created a user-friendly app that sends gentle reminders to drink water."""
    }
)

st.write("<h2 style='color:#40E0D0';>Your Daily Hydration Companion!</h2>",unsafe_allow_html=True)

interval=st.number_input(label="Set Your Limit",step=1,format="%d",min_value=1,help="Specify the maximum number of reminders you want to receive")

hours=st.number_input(label="Set Hourly Interval",step=1,format="%d",min_value=0,help="Specify the number of hours between each hydration reminder.")

minutes=st.number_input(label="Set Minute Interval",step=1,format="%d",min_value=0,help="Specify the number of minutes between each hydration reminder.")

seconds=st.number_input(label="Set Second Interval",step=1,format="%d",min_value=0,help="Specify the number of seconds between each hydration reminder.")

btn=st.button("Set Reminder")

convert=1

if(hours==0 and minutes==0 and seconds==0):
    convert=None

elif hours==0 and minutes>0 and seconds>=0:
    convert=(minutes*60)+seconds

elif hours>0 and minutes==0 and seconds>=0:
    convert=(hours*3600)+seconds

elif hours==0 and minutes==0 and seconds>0:
    convert=seconds

elif hours>0 and minutes>0 and seconds>=0:
    convert=(hours*3600)+(minutes*60)+seconds

if btn:
    if convert!=None:
        for i in range(0,interval):
            time.sleep(convert)
            notification.notify(title='Hydration Reminder', message="It's water o'clock! Take a break and sip your way to better health.", app_icon='water.ico', timeout=0)
    else:
         st.error("Please fill out the above fields!")
