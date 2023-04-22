import streamlit as st
import streamlit.components.v1 as com
import gmaps
from ipywidgets import embed
from PIL import Image
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.mention import mention
import requests
from streamlit_lottie import st_lottie

st.set_page_config(layout="wide")

page_bg_img = """
<style>
# [data-testid="stAppViewContainer"]{
#   background-color: #fff;
# }

[data-testid="stHeader"]{
  background-color: #F97728;
}

[data-testid="stSidebar"]{
  background-color: #FFCEA5;
}

# [data-testid="stHorizontalBlock"]{
#   background-color: #fff;
# }
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)
container = st.container()

with container:
  home1, home2 = st.columns([11,8])
  with home1:
    st.title("We offer a modern solution for detecting Indonesia traditional food by your picture.")
    if st.button("Get Started"):
      switch_page("Let's Try!")
  with home2:
    @st.cache_data
    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    lottie_url = "https://assets5.lottiefiles.com/packages/lf20_dsxct2el.json"
    lottie_json = load_lottieurl(lottie_url)
    st_lottie(lottie_json, height=400)

with container:
  st.subheader("Who We Are?")
  st.write(
    """We are participants of batch two of Internship and Independent Study Certified program. Certified internship program
    is an accelerated program with well-designed learning experiences. Certified independent study is a learning in
    class that is specially designed and made based on the real challenges faced by partners or industry.
  """)

#Location
with container:
  st.header("Location")
  st.subheader("Orbit Future Academy")
  st.write("")
  # Plot coordinates
  # coordinates = (-6.219179776989336, 106.81404408060594)
  # _map = gmaps.figure(center=coordinates, zoom_level=12)

  # # Render map in Streamlit
  # snippet = embed.embed_snippet(views=_map)
  # html = embed.html_template.format(title=" ", snippet=snippet)
  # com.html(html, height=500,width=500)

#Class of Cakes
with container:
  st.title("Indonesia Traditional Cake")
  kue1, kue2, kue3 = st.columns(3)
  with kue1:
    image = Image.open("test/kue_dadar_gulung/5.jpg")
    new_image = image.resize((200,150))
    st.image(new_image, caption="Kue Dadar Gulung")
  with kue2:
    image = Image.open("test/kue_kastengel/0.jpg")
    new_image = image.resize((200,150))
    st.image(new_image, caption="Kue Kastengel")
  with kue3:
    image = Image.open("test/kue_klepon/4.jpg")
    new_image = image.resize((200,150))
    st.image(new_image, caption="Kue Klepon")
  kue4, logo, kue5 = st.columns(3)
  with kue4:
    image = Image.open("test/kue_lapis/5.jpg")
    new_image = image.resize((200,150))
    st.image(new_image, caption="Kue Lapis")
  with logo:
    image = Image.open("img/client-6.webp")
    new_image = image.resize((200,150))
    st.image(new_image, caption="Cake Finder")
  with kue5:
    image = Image.open("test/kue_lumpur/9.jpg")
    new_image = image.resize((200,150))
    st.image(new_image, caption="Kue Lumpur")
  kue6, kue7, kue8 = st.columns(3)
  with kue6:
    image = Image.open("test/kue_putri_salju/0.jpg")
    new_image = image.resize((200,150))
    st.image(new_image, caption="Kue Putri Salju")
  with kue7:
    image = Image.open("test/kue_risoles/0.jpg")
    new_image = image.resize((200,150))
    st.image(new_image, caption="Kue Risoles")
  with kue8:
    image = Image.open("test/kue_serabi/12.jpg")
    new_image = image.resize((200,150))
    st.image(new_image, caption="Kue Serabi")

#Team
with container:
  st.title("Our Team")
  col1, col2, col3, col4, col5 = st.columns(5)
  with col1:
    com.html("""
    <h4 style="font-family:sans-serif; text-align:center;">Athiya Shinta W</h4>
    <p style="font-family:sans-serif; text-align:center;">Cordoba</p>
    <p style="font-family:sans-serif; text-align:center;">Universitas Muhammadiyah Surabaya</p>
    """, height=135)
    mention(
      label="@athiyashinta.w",
      url="https://ig.me/m/athiyashinta.w",
    )
  with col2:
    com.html("""
    <h4 style="font-family:sans-serif; text-align:center;">Halomoan Filipus S</h4>
    <p style="font-family:sans-serif; text-align:center;">Jupyter XXI</p>
    <p style="font-family:sans-serif; text-align:center;">Universitas Telkom</p>
    """, height=135)
    mention(
      label="@moan.fs",
      url="https://ig.me/m/moan.fs",
    )
  with col3:
    com.html("""
    <h4 style="font-family:sans-serif; text-align:center;">Nyayu Chika Marselina</h4>
    <p style="font-family:sans-serif; text-align:center;">Jupyter XXI</p>
    <p style="font-family:sans-serif; text-align:center;">Universitas Sriwijaya</p>
    """, height=135)
    mention(
      label="@nyayuchika",
      url="https://ig.me/m/nyayuchika",
    )
  with col4:
    com.html("""
    <h4 style="font-family:sans-serif; text-align:center;">Sukma Imelda</h4>
    <p style="font-family:sans-serif; text-align:center;">Cordoba</p>
    <p style="font-family:sans-serif; text-align:center;">Universitas Merdeka Malang</p>
    """, height=135)
    mention(
      label="@imld19_",
      url="https://ig.me/m/imld19_",
    )
  with col5:
    com.html("""
    <h4 style="font-family:sans-serif; text-align:center;">Wella Novita Andriani</h4>
    <p style="font-family:sans-serif; text-align:center;">Cordoba</p>
    <p style="font-family:sans-serif; text-align:center;">Universitas Internasional Semen Indonesia</p>
    """, height=135)
    mention(
      label="@wellanvtadr",
      url="https://ig.me/m/wellanvtadr",
    )

#Partner
with container:
  st.title("Our Partner")
  p1,p2,p3,p4,p5,p6,p7,p8,p9 = st.columns(9)
  with p1:
    image = Image.open("img/client-1.png")
    new_image = image.resize((100,100))
    st.image(new_image)
  with p2:
    image = Image.open("img/client-2.png")
    new_image = image.resize((100,100))
    st.image(new_image)
  with p3:
    image = Image.open("img/client-3.png")
    new_image = image.resize((100,100))
    st.image(new_image)
  with p4:
    image = Image.open("img/client-4.png")
    new_image = image.resize((100,100))
    st.image(new_image)
  with p5:
    image = Image.open("img/client-5.png")
    new_image = image.resize((100,100))
    st.image(new_image)
  with p6:
    image = Image.open("img/client-6.webp")
    new_image = image.resize((100,100))
    st.image(new_image)
  with p7:
    image = Image.open("img/client-7.png")
    new_image = image.resize((130,110))
    st.image(new_image)
  with p8:
    image = Image.open("img/client-8.png")
    new_image = image.resize((100,100))
    st.image(new_image)
  with p9:
    image = Image.open("img/client-9.png")
    new_image = image.resize((100,100))
    st.image(new_image)