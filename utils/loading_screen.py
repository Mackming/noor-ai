import streamlit as st
import time

def show_fullscreen_loader(delay: float = 0.5, message: str = "Loading..."):
    pass
'''           
def show_fullscreen_loader(delay: float = 0.5, message: str = "Loading..."):
    with st.empty():
        with st.spinner(message):
            time.sleep(delay)
'''