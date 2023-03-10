import streamlit as st
from PIL import Image
st.radio("what is ur best meme scene?",options=("nirangan garu","venky train scene","padmanabhasimha scene","sontham meme","anaganaga oka pedavaadu","king"))
st.selectbox("what is ur best meme charecter of brammi?",options=("venky train scene","padmanabhasimha scene","king","nellori peddareddy","D"))
st.multiselect("what is ur best meme scene?",options=("nirangan garu","venky train scene","padmanabhasimha scene","sontham meme","anaganaga oka pedavaadu"))

def clicked():
  #print("button cliked")
  pass
st.button("login",on_click=clicked())

def change():
  #print(st.session_state.checker)
  pass
state=st.checkbox("select",on_change=change,key="checker")
if not state:
  st.write("you are unchecked")
else:
  st.write("you are checked")
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
def good():
  return "Why do you care how I am?"
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

st.markdown("""
<style>
.css-1rs6os.edgvbvh3
{
  visibility:hidden
}
</style>
            """,unsafe_allow_html=True)


# def change():
#   print("changed")
# state=st.checkbox("select",on_change=change)
# if not state:
#   st.write("you are unchecked")
# else:
#   st.write("you are checked")
state=st.checkbox("select", value=True)
if state:
  st.write("you are checked")
else:
  st.write("you are unchecked")  

