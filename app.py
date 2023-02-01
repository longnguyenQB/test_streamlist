import streamlit as st
import requests


def main():

    st.title("Sensitive filter")
    message = st.text_input('Enter Text to Classify')

    if st.button('Predict'):
        payload = {
            "text": message
        }
        res = requests.get(f"http://10.10.1.37:10020/predict-text/",params=payload )
        with st.spinner('Classifying, please wait....'):
            st.write(res.json())




if __name__ == '__main__':
    main()