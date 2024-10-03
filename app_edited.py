import streamlit as st
from textblob import TextBlob
from googletrans import Translator

# Inicializar el traductor
translator = Translator()

# Título de la aplicación
st.title('📊 Análisis de Sentimientos con TextBlob')

# Instrucciones en la barra lateral
with st.sidebar:
    st.subheader("Instrucciones")
    st.markdown(
        """
        **Por favor, escribe en el campo de texto la frase que deseas analizar.**
        
        ### Polaridad y Subjetividad
        - **Polaridad:** Indica si el sentimiento expresado es positivo, negativo o neutral. Su valor oscila entre -1 (muy negativo) y 1 (muy positivo).
        - **Subjetividad:** Mide cuánto del contenido es subjetivo (opiniones, emociones) frente a objetivo (hechos). Va de 0 (objetivo) a 1 (subjetivo).
        """
    )

# Expansor para análisis de polaridad y subjetividad
with st.expander('🔍 Analizar Polaridad y Subjetividad'):
    text1 = st.text_area('Escribe tu texto aquí:')
    if text1:
        # Análisis de texto
        blob = TextBlob(text1)
        
        # Resultados de polaridad y subjetividad
        st.subheader('Resultados:')
        st.write(f'**Polaridad:** {round(blob.sentiment.polarity, 2)}')
        st.write(f'**Subjetividad:** {round(blob.sentiment.subjectivity, 2)}')
        
        # Determinación del sentimiento
        polarity = round(blob.sentiment.polarity, 2)
        if polarity >= 0.5:
            st.success('😊 Es un sentimiento Positivo')
        elif polarity <= -0.5:
            st.error('😔 Es un sentimiento Negativo')
        else:
            st.info('😐 Es un sentimiento Neutral')

# Expansor para corrección en inglés
with st.expander('📝 Corrección de Texto en Inglés'):
    text2 = st.text_area('Escribe tu texto en inglés aquí:', key='4')
    if text2:
        blob2 = TextBlob(text2)
        st.write('**Texto corregido:**', blob2.correct())
