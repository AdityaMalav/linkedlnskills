import streamlit as st
import pickle
import numpy as np
from PIL import  Image
import  pandas as pd

with open('final.pkl', 'rb') as file:
    data = pickle.load(file)


image = Image.open('LinkedIn_icon.svg.png')
##Prediction page
skills = ['PYTHON', 'C++', 'JAVA', 'HADOOP', 'SCALA', 'FLASK',
       'PANDAS', 'SPARK', 'NUMPY', 'PHP', 'SQL', 'MYSQL', 'CSS', 'MONGODB',
       'NLTK', 'TENSORFLOW', 'LINUX', 'RUBY', 'JAVASCRIPT', 'DJANGO', 'REACT',
       'REACTJS', 'AI', 'UI', 'TABLEAU', 'NODEJS', 'EXCEL', 'POWER BI',
       'SELENIUM', 'HTML', 'ML']

def show_predict_page():
    st.image(image, width=60)
    st.title(':blue[Linkedin Skills Search]')

    title = st.text_input('Search skill (keyword/s)  👇')
    ok = st.button('Search🔍')

    st.write('_____________________________________________________________________')
    # st.write("""###### Most common Experienve level :""")
    # st.write("""###### Most common Industry :""")
    # st.write("""###### Most common Company class :""")
    # st.write("""###### Total Number of Jobs Available :""")



    for i in skills:

        if (i in skills) and (title.upper() == i):
            industry = data[data[i]==1]['Industry'].mode()
            jobs = data[data[i] == 1]['Employee_count'].count()
            classs = data[data[i] == 1]['Class'].mode()
            experience = data[data[i] == 1]['Level'].mode()

            st.write(f""" Most common Experience level     :     {experience[0]}""")
            st.write(f""" Most common Industry     :     {industry[0]}""")
            st.write(f""" Most common Company class     :     {classs[0]}""")
            st.write(f""" Total Number of Jobs Available     :     {jobs}""")


            if st.button('Look all job postings >'):
                st.dataframe(data[['Name', 'Class', 'Designation', 'Location', 'Total_applicants',
       'LinkedIn_Followers', 'Level', 'Involvement', 'Employee_count',
       'Industry']][data[i]==1])
            break

        if title not in skills:
            st.write("""#### Sorry, Please rewrite skill 😥""")
            break




show_predict_page()

