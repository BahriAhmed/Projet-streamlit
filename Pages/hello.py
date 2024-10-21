import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

st.title('Hello!')
st.header('How are you?')
st.subheader('Fine, thank you')
st.markdown('Merry alone do it burst me songs. Sorry equal charm joy her those folly ham. In they no is many both. Recommend new contented intention improving bed performed age. Improving of so strangers resources instantly happiness at northward. Danger nearer length oppose really add now either. But ask regret eat branch fat garden. Become am he except wishes. Past so at door we walk want such sang. Feeling colonel get her garrets own.')




uploaded_file = st.file_uploader("Upload data")  # Permet à l'utilisateur de télécharger un fichier
if uploaded_file:
    df = pd.read_csv(uploaded_file, encoding='Latin-1')  # Lit le fichier CSV téléchargé avec l'encodage spécifié
    st.dataframe(df)
    # st.table(df)
    st.button('Bonjour!')
    st.checkbox('checkbox')
    st.text_input('Talk to me')
    st.selectbox('Option',['stop','walk'])
    st.slider('minMAX',0,100)

    st.tabs(['cool','cooler','way cooler'])
    st.expander('cool')

    with st.expander("cool"):
        st.write('vert very cool msg')

    st.file_uploader('upload')
    st.download_button('download',data = df.to_csv(),file_name = 'name.csv')



col1, col2, col3 = st.columns(3)

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")
    with st.expander("Fact about cats"):
        st.write("Cats are believed to be the only mammals who don't taste sweetness.")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")
    with st.expander("Fact about dogs"):
        st.write("They can learn over 100 words and gestures")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")
    with st.expander("Fact about owls"):
        st.write("A group of owls is called a parliament.")


fig = plt.figure()
x = [1, 2, 3]
y = np.array([[1, 2], [3, 4], [5, 6]])
plt.plot(x, y)
st.pyplot(fig)



@st.cache_data
def image():
    return st.image("https://static.streamlit.io/examples/owl.jpg")
image()


