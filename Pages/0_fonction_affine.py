# Importation des bibliothèques nécessaires
import streamlit as st  # Streamlit pour créer une interface web interactive
import numpy as np  # Numpy pour les calculs numériques
import matplotlib.pyplot as plt  # Matplotlib pour générer des graphiques

# Fonction pour générer des valeurs dans une plage donnée
def generate_values(minimum, maximum):
    # Utilise np.arange pour créer un tableau de valeurs entre minimum et maximum, avec un pas de 0.5
    x = np.arange(minimum, maximum, 0.5)
    return x 

# Définition d'une fonction affine sous forme de lambda : y = a * x + b
y = lambda x: a * x + b

# Génération des valeurs de x dans la plage [-10, 10]
x = generate_values(-10, 10)

# Titre de l'application Streamlit
st.title("Visualisation interactive d'une fonction affine avec Streamlit")

# Création de deux sliders interactifs pour modifier les valeurs de 'a' et 'b'
a = st.slider('a', 0, 5, 1)  # Slider pour 'a', valeur entre 0 et 5, valeur par défaut 1
b = st.slider('b', 0, 10, 0)  # Slider pour 'b', valeur entre 0 et 10, valeur par défaut 0

# Création de la figure avec Matplotlib
fig = plt.figure()
# Tracé de la fonction affine y(x) avec les paramètres actuels de 'a' et 'b'
plt.plot(y(x))
# Affichage du graphique dans l'application Streamlit
st.pyplot(fig)