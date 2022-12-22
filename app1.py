from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r =  requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets8.lottiefiles.com/private_files/lf30_gvdwzaoj.json")
img_contact_form = Image.open("images/img_contact_form")
img_lottie_animation = Image.open("images/img_lottie_animation")

with st.container():
    st.subheader("Hi, I am Imran :wave:")
    st.title("A Student who is curious about surroundings of the INTERNET")
    st.write("I am a Gamer, Student, Teenager and Foodie. I want to learn Python cause it is a very interesting language.")
    st.write("[Follow me for more >](https://youtube.com/@Red.Lucifer07)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            On my YouTube channel I am creating gameplay videos for people who:
            - are interested to get entertained.
            - want to spend some enjoyable time.
            - loves games but couldn't play.

            If this sounds interesting to you, consider subscribibg my channel and turning on the notification.
            """
        )
        st.write("[YouTube Channel >](https://youtube.com/@Red.Lucifer07)")
with right_column:
    st_lottie(lottie_coding, height=300, key="gaming")


with st.container():
    st.write("---")
    st.header("My Videos")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("GTA V Gaming Test | AMD Ryzen 5 3500U | Vega 8 | 8GB Ram |")
        st.write(
            """
            So in this video I am going to run GTA V on a Vega 8 gfx laptop. Watch the full video to see how the game works on an minimum requirements laptop or PC.

            Follow me on-

            Instagram- [Recently Deleted]

            And if you want to suggest me any games then comment or else DM me on Instagram.

            Editing App- Kinemaster

            My Specs-

            Phone- Realme C11 2021 [4GB Ram/64GB Rom]

            Laptop- Acer Aspire 3 
            [8GB Ram]
            [512GB SSD]
            [AMD Ryzen 5 3500U]
            [Windows 11]

            Keyboard And Mouse- Zebronics Zeb Transformer [White and Silver]
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/YkjSBsu9jFY)")
