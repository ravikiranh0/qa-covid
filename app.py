#cdqa_pipeline.to('cpu')
#joblib.dump(cdga_pipeline, './models/bert_qa_custom.joblib')
import requests
import streamlit as st
import joblib
import time
st.set_option( 'deprecation.showfileUploaderEncoding', False)
st.title("COVID-19 Question Answering Webapp")
st.text("Get accurate information regargding coronavirus!")

# @st.cache(allow_output_mutation=True)
# def load_model():
#     model=joblib.load('bert_qa_custom.joblib')
#     return model

# with st.spinner('Loading Model Into Memory....'):
#     model = load_model()

text = st.text_input('Enter your questions here..')

if text:
    st.write("Response :")
    with st.spinner( 'Searching for answers.....'):
        time.sleep(15)
        st.balloons()
        st.write('answer: {}'.format("")
        st.write('title: {}'.format("")
        st.write('paragraph: {}'.format("")
    st.write("")
