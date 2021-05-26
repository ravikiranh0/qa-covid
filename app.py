#cdqa_pipeline.to('cpu')
#joblib.dump(cdga_pipeline, './models/bert_qa_custom.joblib')
import requests
import streamlit as st
import joblib
import time
st.set_option( 'deprecation.showfileUploaderEncoding', False)
st.title("COVID-19 Question Answering Webapp")
st.text("Get accurate information regargding coronavirus!")
st.spinner('Loading Model Into Memory....')
# @st.cache(allow_output_mutation=True)
# def load_model():
#     model=joblib.load('bert_qa_custom.joblib')
#     return model


    # print("loading")
#     model = load_model()

text = st.text_input('Enter your questions here..')
# with st.spinner('Searching'):
#     time.sleep(5)
#     st.balloons()
if text:
    st.write("Response :")
    with st.spinner( 'Searching for answers.....'):
        time.sleep(15)
        st.balloons()
        # prediction = model.predict(text)
        st.write('answer: {}'.format(""))
        st.write('title: {}'.format(""))
        st.write('paragraph: {}'.format(""))
    st.write("")
