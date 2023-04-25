import streamlit as st
from PIL import Image

st.set_page_config(page_title='About Cake Finder', page_icon='img/logo-cakefinder.jpg', layout='wide')

page_bg_img = """
<style>
[data-testid="stAppViewContainer"]{
  background-image: linear-gradient(to bottom right, #c0fdff, #cddafd);
}

[data-testid="stHeader"]{
  background-color: #778da9;
}

</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

container = st.container()

with container:
  st.markdown("<h2 style='font-family:sans-serif; text-align:center; margin-bottom:0;'>What is Cake Finder?</h2>", unsafe_allow_html=True)
  st.write(
    """We are participants of batch two of Internship and Independent Study Certified program. Certified internship program
    is an accelerated program with well-designed learning experiences. Certified independent study is a learning in
    class that is specially designed and made based on the real challenges faced by partners or industry.
  """)
  st.write(" ")
  st.write(" ")
  st.write(" ")
  st.write(" ")
  st.write(" ")

#Class of Cakes
with container:
  st.markdown("<h5 style='font-family:sans-serif; text-align:center; margin-bottom:0;'>Class of</h5>", unsafe_allow_html=True)
  st.markdown("<h2 style='font-family:sans-serif; text-align:center; margin:0; padding-top:0;'>Indonesia Traditional Cakes</h2>", unsafe_allow_html=True)
  none, kue1, kue2, kue3, none2 = st.columns(5)
  with none:
    st.write(" ")
  with kue1:
    # st.markdown("<img src:'test/kue_dadar_gulung/5.jpg' style:'display:block; margin-left:auto; margin-right:auto; width:50%;'>", unsafe_allow_html=True)
    image = Image.open("test/kue_dadar_gulung/5.jpg")
    new_image = image.resize((200,150))
    st.image(new_image, use_column_width=True)
    st.markdown("<p style='font-family:sans-serif; text-align:center;'>Dadar Gulung</p>", unsafe_allow_html=True)
  with kue2:
    image = Image.open("test/kue_kastengel/0.jpg")
    new_image = image.resize((200,150))
    st.image(new_image, use_column_width=True)
    st.markdown("<p style='font-family:sans-serif; text-align:center;'>Kastengel</p>", unsafe_allow_html=True)
  with kue3:
    image = Image.open("test/kue_klepon/4.jpg")
    new_image = image.resize((200,150))
    st.image(new_image, use_column_width=True)
    st.markdown("<p style='font-family:sans-serif; text-align:center;'>Klepon</p>", unsafe_allow_html=True)
  with none2:
    st.write(" ")
  none3, kue4, logo, kue5, none4 = st.columns(5)
  with none3:
    st.write(" ")
  with kue4:
    image = Image.open("test/kue_lapis/5.jpg")
    new_image = image.resize((200,150))
    st.image(new_image, use_column_width=True)
    st.markdown("<p style='font-family:sans-serif; text-align:center;'>Lapis</p>", unsafe_allow_html=True)
  with logo:
    image = Image.open("img/logo-cakefinder.jpg")
    new_image = image.resize((200,150))
    st.image(new_image, use_column_width=True)
    st.markdown("<p style='font-family:sans-serif; text-align:center;'>Cake Finder</p>", unsafe_allow_html=True)
  with kue5:
    image = Image.open("test/kue_lumpur/9.jpg")
    new_image = image.resize((200,150))
    st.image(new_image, use_column_width=True)
    st.markdown("<p style='font-family:sans-serif; text-align:center;'>Lumpur</p>", unsafe_allow_html=True)
  with none4:
    st.write(" ")
  none5, kue6, kue7, kue8, none6 = st.columns(5)
  with none5:
    st.write(" ")
  with kue6:
    image = Image.open("test/kue_putri_salju/0.jpg")
    new_image = image.resize((200,150))
    st.image(new_image, use_column_width=True)
    st.markdown("<p style='font-family:sans-serif; text-align:center;'>Putri Salju</p>", unsafe_allow_html=True)
  with kue7:
    image = Image.open("test/kue_risoles/0.jpg")
    new_image = image.resize((200,150))
    st.image(new_image, use_column_width=True)
    st.markdown("<p style='font-family:sans-serif; text-align:center;'>Risoles</p>", unsafe_allow_html=True)
  with kue8:
    image = Image.open("test/kue_serabi/12.jpg")
    new_image = image.resize((200,150))
    st.image(new_image, use_column_width=True)
    st.markdown("<p style='font-family:sans-serif; text-align:center;'>Serabi</p>", unsafe_allow_html=True)
  with none6:
    st.write(" ")