import streamlit as st
import serial
import plotly.graph_objects as go
import time
import random as r
arduino = serial.Serial(port='COM3', baudrate=9600)
def bv(c):
    fig3 = go.Figure(go.Indicator(
        domain = {'x': [0, 1], 'y': [0, 1]},
        value =c ,
        mode = "gauge+number",
        title = {'text': "BATTERY VOLTAGE"},
    
        gauge = {'axis': {'range': [None, 50]},
             'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 490}}))
    st.plotly_chart(fig3)

st.header("SOLAR POWERED EV CHARGING STATION")

try:
    arduino.open()
except:
    pass
while True:
    arduino.flushInput()
    arduino.flushOutput()
    arduino.flush()
    try:
        val = arduino.readline().decode().strip('\r\n').split('*')[1]
    except:
        val = 0
    bv(val)
    time.sleep(0.05)
   

