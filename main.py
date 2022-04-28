"""The :mod:`streamlit_app` serves as a demo application to show the scoring API system at work.
This runs on sreamlit
"""
# Author: Christopher Dare
import json

import pandas as pd
import requests
import streamlit as st

base_url = "https://jamzee-cotp-api.herokuapp.com/api"

st.title("Jamzee's Adventure")
st.write(
    """Earn money whilst you sleep with our COTPs bot"""
)  # description

burn_area = ""
st.title("Jamzee's COTPS automation")

username = st.text_input("username")
password = st.text_input("password")

if st.button("Start automation"):
    login_data = dict()
    login_data["username"] = str(username)
    login_data["password"] = str(password)

    payload = json.dumps(login_data)
    st.write(f"Attempting login... for f{username}")
    response = requests.post(f"{base_url}/v1/login/cotps-user", data=payload)
    print(response)
    print(response.status_code)
    data = response.json()
    output = "Done"
    # if data["success"]:
    #     burn_area = data["payload"]
    #     burn_area = round(burn_area, 2)
    #     if burn_area > 0:
    #         output = f"Burn area is {burn_area}"
    #     else:
    #         output = f"No fire, congratulations"

    st.title(output)
