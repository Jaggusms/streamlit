import streamlit as st
from PIL import Image
st.title("welocome to streamlit")
st.subheader("hi i am subhear")
st.header("i am header")
st.text("i am text")
st.markdown("**hello** hello is bold. *word* is iatic")
st.markdown("[campusx](https://github.com/campusx-official)")
st.markdown("![kajal](./kajal.jpg)",unsafe_allow_html=True)

# img_to_bytes and img_to_html inspired from https://pmbaumgartner.github.io/streamlitopedia/sizing-and-images.html
import base64
from pathlib import Path
def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded
def img_to_html(img_path):
    img_html = "<img src='data:image/png;base64,{}' class='img-fluid'>".format(
      img_to_bytes(img_path)
    )
    return img_html
st.markdown(img_to_html('kajal.jpg'), unsafe_allow_html=True)

image = Image.open('kajal.jpg')
st.image(image, caption='kajal')

st.latex(r"\begin{pmatrix}a & b \\c & d\end{pmatrix}")

st.json({1:"1,2",2:"2"})
code="""
print("hey missu how are you")
def yours():
  return "because, i am yours and you are ..."
def good():
  return "Why do you care how I am?"+yours()
"""
st.code(code,language="python")
# we can use write instead of markdown
st.write("## Hi")
st.metric(label="wind speed",value="120ms^-1" ,delta="1.4ms^-1 ")
st.metric(label="wind speed",value="120ms^-1" ,delta="-1.4ms^-1 ")
import pandas as pd
table=pd.DataFrame({"c1":[0,1,2],"c2":[2,1,0]})
st.table(table)
st.dataframe(table)

st.audio("ye_mere_rajaha.mp3")
st.audio("Aduvari _Matalaku.mp3")
st.video("ammaye_sannaga.mp4")
