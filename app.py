from textblob import TextBlob
import streamlit as st 
# This is the Title and Description of the App
st.title("Sentiment Analyser ")
st.subheader("This is a Basics Sentence Analyser that Uses TextBlob Library to Analyse your Text.")

# This Takes the Input from the User 
text = st.text_input("Enter your Input here")
st.write("Press Get Polarity to Get Whether the sentece is Postive, Negative or Neutral")
polaritychk = st.button(label="Get Polartity")
subjectivitychk = st.button(label="Get Subjectivity")
result = isinstance(text, str)

if polaritychk:  
    st.write("This is the Polarity of your sentence ..")
    blob = TextBlob(text)
    polarity = blob.polarity
    if polarity==0:
        st.write("The Sentence is Neutral .. ")
    elif polarity>0:
        st.write("The Sentence is Postive .. ")
    else:
        st.write("The Sentence is Negative ..")  


elif subjectivitychk:
    st.write("This is the Subjectivity of your Sentence ..")
    blob = TextBlob(text)
    subjectivity = blob.subjectivity
    if (subjectivity==0.50) or subjectivity>0.30:
        st.write("The sentence is Fairly Subjective ..")
    elif (subjectivity>0.75):
        st.write("The Sentence is Subjective ..")
    elif (subjectivity<0.30):
        st.write("The Sentence is Not Subjective ..")
    else:
        st.write("The Sentence is Too Subjective")
