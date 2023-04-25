import streamlit as st
from PIL import Image
import webbrowser
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title='About Cake Finder', page_icon='img/logo-cakefinder.jpg')

page_bg_img = """
<style>
[data-testid="stAppViewContainer"]{
  background-image: linear-gradient(to bottom right, #c0fdff, #cddafd);
}

[data-testid="stHeader"]{
  background-color: #778da9;
}

.stButton>button {
  color: #000;
  border-radius: 10%;
  backgroud-color: #00ff00;
}

</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

container = st.container()

with container:
  st.markdown("<h2 style='font-family:sans-serif; text-align:center; margin-bottom:0;'>What is Cake Finder?</h2>", unsafe_allow_html=True)
  st.markdown("""
  <p style='font-family:sans-serif; text-align:justify; margin:0; padding-top:0;'>
    Cake Finder is a website for classifying Indonesia traditional cakes by image. There are 8 classes in Indonesia
    traditional cakes in this website such as dadar gulung, kastengel, klepon, lapis, lumpur, putri salju, 
    risoles, and serabi.
  </p>"""
  , unsafe_allow_html=True)
  st.write(" ")
  if st.button("Let's Try!"):
      switch_page("Let's Try!")
  st.write(" ")
  st.write(" ")
  st.write(" ")
  st.write(" ")
  st.write(" ")

#Class of Cakes
with container:
  st.markdown("<h5 style='font-family:sans-serif; text-align:center; margin-bottom:0;'>Class of</h5>", unsafe_allow_html=True)
  st.markdown("<h2 style='font-family:sans-serif; text-align:center; margin:0; padding-top:0;'>Indonesia Traditional Cakes</h2>", unsafe_allow_html=True)
  kue1, kue2, kue3 = st.columns(3)
  with kue1:
    # st.markdown("<img src:'test/kue_dadar_gulung/5.jpg' style:'display:block; margin-left:auto; margin-right:auto; width:50%;'>", unsafe_allow_html=True)
    image = Image.open("test/kue_dadar_gulung/5.jpg")
    new_image = image.resize((200,150))
    st.image(new_image, use_column_width=True)
    st.markdown("<p style='font-family:sans-serif; text-align:center;'><a href='https://en.wikipedia.org/wiki/Dadar_gulung'>Dadar Gulung</a></p>", unsafe_allow_html=True)
    # if st.button('Read More'):
    #   webbrowser.open_new_tab('https://id.wikipedia.org/wiki/Dadar_gulung')
  with kue2:
    image = Image.open("test/kue_kastengel/0.jpg")
    new_image = image.resize((200,150))
    st.image(new_image, use_column_width=True)
    st.markdown("<p style='font-family:sans-serif; text-align:center;'><a href='https://en.wikipedia.org/wiki/Kaasstengels'>Kastengel</a></p>", unsafe_allow_html=True)
  with kue3:
    image = Image.open("test/kue_klepon/4.jpg")
    new_image = image.resize((200,150))
    st.image(new_image, use_column_width=True)
    st.markdown("<p style='font-family:sans-serif; text-align:center;'><a href='https://en.wikipedia.org/wiki/Klepon'>Klepon</a></p>", unsafe_allow_html=True)
  kue4, logo, kue5 = st.columns(3)
  with kue4:
    image = Image.open("test/kue_lapis/10.jpg")
    new_image = image.resize((200,150))
    st.image(new_image, use_column_width=True)
    st.markdown("<p style='font-family:sans-serif; text-align:center;'><a href='https://en.wikipedia.org/wiki/Kue_lapis'>Lapis</a></p>", unsafe_allow_html=True)
  with logo:
    image = Image.open("img/logo-cakefinder.jpg")
    new_image = image.resize((200,150))
    st.image(new_image, use_column_width=True)
    st.markdown("<p style='font-family:sans-serif; text-align:center;'>Cake Finder</p>", unsafe_allow_html=True)
  with kue5:
    image = Image.open("test/kue_lumpur/9.jpg")
    new_image = image.resize((200,150))
    st.image(new_image, use_column_width=True)
    st.markdown("<p style='font-family:sans-serif; text-align:center;'><a href='https://id.wikipedia.org/wiki/Kue_lumpur'>Lumpur</a></p>", unsafe_allow_html=True)
  kue6, kue7, kue8 = st.columns(3)
  with kue6:
    image = Image.open("test/kue_putri_salju/0.jpg")
    new_image = image.resize((200,150))
    st.image(new_image, use_column_width=True)
    st.markdown("<p style='font-family:sans-serif; text-align:center;'><a href='https://en.wikipedia.org/wiki/Kue_putri_salju'>Putri Salju</a></p>", unsafe_allow_html=True)
  with kue7:
    image = Image.open("test/kue_risoles/0.jpg")
    new_image = image.resize((200,150))
    st.image(new_image, use_column_width=True)
    st.markdown("<p style='font-family:sans-serif; text-align:center;'><a href='https://en.wikipedia.org/wiki/Rissole'>Risoles</a></p>", unsafe_allow_html=True)
  with kue8:
    image = Image.open("test/kue_serabi/12.jpg")
    new_image = image.resize((200,150))
    st.image(new_image, use_column_width=True)
    st.markdown("<p style='font-family:sans-serif; text-align:center;'><a href='https://en.wikipedia.org/wiki/Serabi'>Serabi</a></p>", unsafe_allow_html=True)