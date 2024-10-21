# Importation des bibliothèques nécessaires
import streamlit as st  # Pour créer une application web interactive
import pandas as pd  # Pour manipuler les données en DataFrame
import seaborn as sns  # Pour la visualisation des données
import matplotlib.pyplot as plt  # Pour créer des graphiques
import numpy as np # pour créer les arrays
import io  # Pour gérer les flux d'entrée/sortie

# Fonction pour obtenir les colonnes numériques
def numericColmuns(df: pd.DataFrame) -> list:
    result = []
    for i in df.columns:
        if pd.api.types.is_numeric_dtype(df[i]):  # Vérifie si la colonne est numérique
            result.append(i)  # Ajoute la colonne à la liste des résultats
    return result



# Fonction pour explorer les données
def explore(df: pd.DataFrame):
    st.header("Exploration des données")  # Titre de la section
    st.write(df.head())  # Affiche les 5 premières lignes du DataFrame
    st.write(df.describe())  # Affiche des statistiques descriptives du DataFrame
    select = st.multiselect('Select columns', df.columns)  # Sélection multiple des colonnes
    st.write(df[select])  # Affiche les données des colonnes sélectionnées

# Fonction pour visualiser les données
def visualiseScatter(df: pd.DataFrame):
    st.header("Visualisation des données (Scatter Plot)")  # Titre de la section
    graphselects = st.multiselect('Select columns', df.columns, max_selections=2,key='multiselect1')  # Sélection de colonnes pour le graphique
    
    if(len(graphselects) == 2):
            fig = plt.figure()  # Création d'une nouvelle figure
            sns.scatterplot(x = df[graphselects[0]],y = df[graphselects[1]])  # Trace un nuage de points
            st.pyplot(fig)  # Affiche le graphique dans l'application
   
def visualiseBar(df:pd.DataFrame):
    st.header("Visualisation des données (Bar Plot)")  # Titre de la section
    selectNum = st.multiselect('Select numeric column', numericColmuns(df), max_selections=1)
    fig = plt.figure()  # Création d'une nouvelle figure
    if selectNum:
        y = df[selectNum].to_numpy()
        y = y.flatten()
        plt.bar(x = df.index,height = y) 
        st.pyplot(fig)  # Affiche le graphique dans l'application

def visualisePie(df:pd.DataFrame):
    st.header("Visualisation des données (Pie)")  # Titre de la section
    selectNum = st.multiselect('Select numeric column', numericColmuns(df), max_selections=1)
    fig = plt.figure()  # Création d'une nouvelle figure
    if selectNum:
        y = df[selectNum].to_numpy().flatten()
        plt.pie(y) 
        st.pyplot(fig)  # Affiche le graphique dans l'application

def visualiseCourbe(df:pd.DataFrame):
    st.header("Visualisation des données (Courbe)")  # Titre de la section
    selectNum = st.multiselect('Select numeric column', numericColmuns(df), max_selections=1)
    fig = plt.figure()  # Création d'une nouvelle figure
    if selectNum:
        plt.plot(df[selectNum]) 
        st.pyplot(fig)  # Affiche le graphique dans l'application


# Fonction pour filtrer les données
def Filter(df: pd.DataFrame):
    st.header("Filtrage des données")  # Titre de la section
    selectCulumn = st.multiselect('Select column', df.columns, max_selections=1)  # Sélection d'une colonne
    try:
        selectData = st.multiselect('Select datapoint', df[selectCulumn[0]], max_selections=1)  # Sélection des points de données
        st.dataframe(df[df[selectCulumn[0]] == selectData[0]])  # Affiche les lignes filtrées
    except:
        pass  # Ignore les erreurs si aucune colonne n'est sélectionnée



# Fonction pour afficher un histogramme
def Histogramme(df: pd.DataFrame):
    st.header("Histogramme")  # Titre de la section
    selectNum = st.multiselect('Select numeric column', numericColmuns(df), max_selections=1)  # Sélection d'une colonne numérique
    bac = st.slider('Bacs number', 1, 40)  # Slider pour sélectionner le nombre de bacs
    fig2 = plt.figure()  # Création d'une nouvelle figure
    plt.hist(df[selectNum], bins=bac)  # Crée l'histogramme avec le nombre de bacs sélectionné
    st.pyplot(fig2)  # Affiche l'histogramme

# Fonction pour afficher un résumé des données
def info(df: pd.DataFrame):
    st.header("Résumé des données")  # Titre de la section
    buffer = io.StringIO()  # Crée un flux pour stocker les informations
    df.info(buf=buffer)  # Écrit les informations du DataFrame dans le buffer
    info_output = buffer.getvalue()  # Récupère les informations sous forme de chaîne
    st.text(info_output)  # Affiche les informations dans l'application

def choix():
    st.header('Visualisation')
    figs = ['scatter','bar','hist','pie','courbe' ]
    return st.multiselect("sélectionner le style de courbe",figs)

def Multyplot(df,list):
    if 'scatter' in list:
        visualiseScatter(df)
    if 'bar' in list:
        visualiseBar(df)
    if 'hist' in list:
        Histogramme(df)
    if 'pie' in list:
        visualisePie(df)
    if 'courbe' in list:
        visualiseCourbe(df)
    

# Titre de l'application
st.title("Création d'un outil d'analyse de données interactif avec Streamlit")

# Chargement du fichier de données par l'utilisateur
uploaded_file = st.file_uploader("Upload data")  # Permet à l'utilisateur de télécharger un fichier
if uploaded_file:
    df = pd.read_csv(uploaded_file, encoding='Latin-1')  # Lit le fichier CSV téléchargé avec l'encodage spécifié
    
    # Appelle des fonctions 
    explore(df)
    Filter(df)
    info(df)
    Multyplot(df,choix())