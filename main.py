"""The :mod:`streamlit_app` serves as a demo application to show the scoring API system at work.
This runs on sreamlit
"""
# Author: Christopher Dare
import json
import websockets

import pandas as pd
import requests
import streamlit as st

base_url = "https://jamzee-cotp-api.herokuapp.com/api"
ws_base_url = "ws://jamzee-cotp-api.herokuapp.com"

st.image('./logo.png')
st.title("Earn money whilst you sleep with our COTPs bot")


burn_area = ""

username = st.text_input("username").strip()
password = st.text_input("password").strip()


async def process_automation(username: str, password: str):
    websocket = websockets.connect(uri=f"{base_url}/ws/automations/actions")
    event = {
        "username": username,
        "password": password
    }
    st.write(f"Commencing automation for {username}")
    st.write(f"Establishing connection....")
    event["type"] = "websocket.send"
    websocket.send(json.dumps(event))

    st.write(f"Receiving messages connection....")
    while True:
        message = await websocket.recv()
        st.write(message)


if st.button("Start automation"):
    login_data = dict()
    # login_data["username"] = str(username).strip()
    # login_data["password"] = str(password).strip()
    # payload = json.dumps(login_data)
    process_automation(username=username, password=password)

    # response = requests.post(f"{base_url}/v1/login/cotps-user", data=payload)
    # st.write(response.status_code)
    # data = response.json()
    # st.write(data)
    output = "Done"
    # if data["success"]:
    #     burn_area = data["payload"]
    #     burn_area = round(burn_area, 2)
    #     if burn_area > 0:
    #         output = f"Burn area is {burn_area}"
    #     else:
    #         output = f"No fire, congratulations"

    st.title(output)
