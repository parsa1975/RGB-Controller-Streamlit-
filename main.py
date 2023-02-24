import streamlit as st
import package as pk
st.title("LightApp")
PORT = st.selectbox(label = "Select COM-Port",options = range(1,31))
ConnectButton = st.button(label = "Connect",help = "Select Your Com Port And Click To Connect Button.")
if ConnectButton:
    e = False
    try:
        pk.Connect("COM"+str(PORT))
    except:
        e = True
    if e:
        st.error("Port not founded.")
    else:
        st.success("Connected!")
st.write("Controll Page")
RH = st.button("Red-ON")
RL = st.button("Red-OFF")
GH = st.button("Green-ON")
GL = st.button("Green-OFF")
BH = st.button("Blue-ON")
BL = st.button("Blue-OFF")
if RH:
    pk.R(True)
if RL:
    pk.R(False)
if GH:
    pk.G(True)
if GL:
    pk.G(False)
if BH:
    pk.B(True)
if BL:
    pk.B(False)