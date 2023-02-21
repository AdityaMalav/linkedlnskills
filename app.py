import streamlit as st
import pickle
import numpy as np
from PIL import  Image
import  pandas as pd

with open('final.pkl', 'rb') as file:
    data = pickle.load(file)

st.set_page_config(layout="centered")


image = Image.open('LinkedIn_icon.svg.png')
# pics = ['m.png','g.png','aditya.png','s.jpeg']
# pics_name = ["Manish Hemnani "
#              "(pd16_309)", "Gareema Tom  (pd16_147)", "Aditya Malav (pd16_309)", "Mohammad Sohal (pd16_139)"]

##Prediction page
skills = ['PYTHON', 'C++', 'JAVA', 'HADOOP', 'SCALA', 'FLASK',
       'PANDAS', 'SPARK', 'NUMPY', 'PHP', 'SQL', 'MYSQL', 'CSS', 'MONGODB',
       'NLTK', 'TENSORFLOW', 'LINUX', 'RUBY', 'JAVASCRIPT', 'DJANGO', 'REACT',
       'REACTJS', 'AI', 'UI', 'TABLEAU', 'NODEJS', 'EXCEL', 'POWER BI',
       'SELENIUM', 'HTML', 'ML']

def show_predict_page():
    title_container = st.container()
    col1,mid, col2 = st.columns([1,2.6, 32])
    with col1:
        st.image(image, width=70)
    with col2:
        st.markdown('<h1 style="color: skyblue;"> Linkedin Skills  Search</h1>',
                    unsafe_allow_html=True)

    # st.title(':blue[Linkedin Skills Search]')

    title = st.text_input('Search skill (keyword/s)  👇')
    ok = st.button('Search🔍')

    st.write('_____________________________________________________________________')


    for i in skills:

        ###Write skill
        i= title.upper()
        if (i in skills):
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

        ##Noting write
        if i=='':
            st.write("""### A warm Welcome , Please write a skill.......""")
            break

        ##masai
        if i=='MASAI':
            st.write("""##### Sorry,"""
                     " [Masai](https://masaischool.com/)"
                     " is not a skill but it's a skill building platform and an outcome driven career school. "
                     "They introduce a new model of higher education in which they, Masai, invest in their students’ future and success.......")
            break

        ###team
        if i in ['TEAM','MY TEAM']:
        #     st.image(pics, width=146, caption=pics_name)
        #     break
            col1, col2,col3,col4 = st.columns(4)

            manish = Image.open('m.png')
            col1.image(manish, use_column_width=True)
            col1.write("""##### [Manish Hemnani](https://www.linkedin.com/in/manish-hemnani-280953179/)""")
            col1.write('''###### pd16_216''')

            g = Image.open('g.png')
            col2.image(g ,use_column_width=True)
            col2.write(f"""##### [Greeshma Tom](https://www.linkedin.com/in/greeshma-tom-454a57237/)""")
            col2.write('''###### pd16_146''')

            aditya = Image.open('aditya.png')
            col3.image(aditya, use_column_width=True)
            col3.markdown("""##### [ Aditya Malav](https://www.linkedin.com/in/adityamalav/)""",unsafe_allow_html=True )
            col3.write('''###### pd16_309''')

            s = Image.open('s.jpeg')
            col4.image(s, use_column_width=True)
            col4.write("""##### [ Mohammad Sohal](https://www.linkedin.com/in/mohammad-sohal-5b8b38224/)""")
            col4.write('''###### pd16_139''')
            break



        ###wrong skill
        else:
            st.write("""#### Sorry, Please rewrite skill 😥""")
            break




show_predict_page()


