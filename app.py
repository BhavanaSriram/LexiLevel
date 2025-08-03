import streamlit as st
import textstat

st.set_page_config(page_title="LexiLevel – Readability Analyzer", page_icon="📘")

st.title("📘 LexiLevel – Text Readability Analyzer")
st.write("Enter any text below to analyze how easy or hard it is to read.")

text = st.text_area("📝 Enter your text here:", height=200)

if st.button("Analyze Readability"):
    if text.strip() == "":
        st.warning("Please enter some text first.")
    else:
        st.subheader("🔍 Readability Scores")
        st.write(f"**Flesch Reading Ease:** {textstat.flesch_reading_ease(text):.2f}")
        st.write(f"**Gunning Fog Index:** {textstat.gunning_fog(text):.2f}")
        st.write(f"**SMOG Index:** {textstat.smog_index(text):.2f}")
        st.write(f"**Coleman-Liau Index:** {textstat.coleman_liau_index(text):.2f}")
        st.write(f"**Automated Readability Index:** {textstat.automated_readability_index(text):.2f}")
        st.success(f"📚 Estimated Grade Level: {textstat.text_standard(text)}")


