import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.mention import mention
import requests
from streamlit_lottie import st_lottie
import streamlit.components.v1 as components

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

def local_css(filename):
  with open(filename) as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

local_css("css/style.css")

container = st.container()

with container:
  home1, home2 = st.columns([11,8])
  with home1:
    st.title("We offer a modern solution for detecting Indonesia traditional cake by your picture.")
    if st.button("Get Started"):
      switch_page("Let's Try!")
  with home2:
    @st.cache_data
    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    lottie_url = "https://assets6.lottiefiles.com/packages/lf20_bpqri9y8.json"
    lottie_json = load_lottieurl(lottie_url)
    st_lottie(lottie_json, height=400)
  st.write(" ")
  st.write(" ")
  st.write(" ")
  st.write(" ")
  st.write(" ")

with container:
  who1, who2 = st.columns([11,8])
  with who1:
    st.subheader("Who We Are?")
    st.write(
      """We are participants of batch two of Internship and Independent Study Certified program. Certified internship program
      is an accelerated program with well-designed learning experiences. Certified independent study is a learning in
      class that is specially designed and made based on the real challenges faced by partners or industry.
    """)
  with who2:
    st.image(Image.open("img/bg-orbit.jpg"))
  st.write(" ")
  st.write(" ")
  st.write(" ")
  st.write(" ")
  st.write(" ")

#Location
with container:
  st.markdown("<h5 style='font-family:sans-serif; text-align:center; margin-bottom:0;'>Location</h5>", unsafe_allow_html=True)
  st.markdown("<h2 style='font-family:sans-serif; text-align:center; margin:0; padding-top:0;'>Orbit Future Academy</h2>", unsafe_allow_html=True)
  loc1, loc2 = st.columns([0.4,10])
  with loc1:
    st.image(Image.open("img/loc.png"))
  with loc2:
    st.write("""Veteran RI Building 15th Floor Plaza Semanggi, Jl. Jend. Sudirman No.Kav. 50, 
    RT.1/RW.4, Karet Semanggi, Kecamatan Setiabudi, Kota Jakarta Selatan, Daerah Khusus Ibukota Jakarta 
    12930""")
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
    st.markdown("<p style='font-family:sans-serif; text-align:center;'>Kue Dadar Gulung</p>", unsafe_allow_html=True)
  with kue2:
    image = Image.open("test/kue_kastengel/0.jpg")
    new_image = image.resize((200,150))
    st.image(new_image, use_column_width=True)
    st.markdown("<p style='font-family:sans-serif; text-align:center;'>Kue Kastengel</p>", unsafe_allow_html=True)
  with kue3:
    image = Image.open("test/kue_klepon/4.jpg")
    new_image = image.resize((200,150))
    st.image(new_image, use_column_width=True)
    st.markdown("<p style='font-family:sans-serif; text-align:center;'>Kue Klepon</p>", unsafe_allow_html=True)
  with none2:
    st.write(" ")
  none3, kue4, logo, kue5, none4 = st.columns(5)
  with none3:
    st.write(" ")
  with kue4:
    image = Image.open("test/kue_lapis/5.jpg")
    new_image = image.resize((200,150))
    st.image(new_image, use_column_width=True)
    st.markdown("<p style='font-family:sans-serif; text-align:center;'>Kue Lapis</p>", unsafe_allow_html=True)
  with logo:
    image = Image.open("img/logo-cakefinder.jpg")
    new_image = image.resize((200,150))
    st.image(new_image, use_column_width=True)
    st.markdown("<p style='font-family:sans-serif; text-align:center;'>Cake Finder</p>", unsafe_allow_html=True)
  with kue5:
    image = Image.open("test/kue_lumpur/9.jpg")
    new_image = image.resize((200,150))
    st.image(new_image, use_column_width=True)
    st.markdown("<p style='font-family:sans-serif; text-align:center;'>Kue Lumpur</p>", unsafe_allow_html=True)
  with none4:
    st.write(" ")
  none5, kue6, kue7, kue8, none6 = st.columns(5)
  with none5:
    st.write(" ")
  with kue6:
    image = Image.open("test/kue_putri_salju/0.jpg")
    new_image = image.resize((200,150))
    st.image(new_image, use_column_width=True)
    st.markdown("<p style='font-family:sans-serif; text-align:center;'>Kue Putri Salju</p>", unsafe_allow_html=True)
  with kue7:
    image = Image.open("test/kue_risoles/0.jpg")
    new_image = image.resize((200,150))
    st.image(new_image, use_column_width=True)
    st.markdown("<p style='font-family:sans-serif; text-align:center;'>Kue Risoles</p>", unsafe_allow_html=True)
  with kue8:
    image = Image.open("test/kue_serabi/12.jpg")
    new_image = image.resize((200,150))
    st.image(new_image, use_column_width=True)
    st.markdown("<p style='font-family:sans-serif; text-align:center;'>Kue Serabi</p>", unsafe_allow_html=True)
  with none6:
    st.write(" ")
  st.write(" ")
  st.write(" ")
  st.write(" ")
  st.write(" ")
  st.write(" ")

#Team
with container:
  st.markdown("<h5 style='font-family:sans-serif; text-align:center; margin-bottom:0;'>Team</h5>", unsafe_allow_html=True)
  st.markdown("<h2 style='font-family:sans-serif; text-align:center; margin:0; padding-top:0;'>Our Team</h2>", unsafe_allow_html=True)
  col1, col2, col3, col4, col5 = st.columns(5)
  with col1:
    st.image(Image.open("team/3.png"), use_column_width=True)
    st.markdown("<h5 style='font-family:sans-serif; text-align:center;'>Athiya Shinta W</h5>" ,unsafe_allow_html=True)
    st.markdown("<p style='font-family:sans-serif; text-align:center;'>Cordoba</p>" ,unsafe_allow_html=True)
    st.markdown("<p style='font-family:sans-serif; text-align:center; line-height:20px;'><i>Universitas Muhammadiyah Surabaya</i></p>", unsafe_allow_html=True)
    mention(
      label="@athiyashinta.w",
      url="https://ig.me/m/athiyashinta.w",
    )
  with col2:
    st.image(Image.open("team/2.png"), use_column_width=True)
    st.markdown("<h5 style='font-family:sans-serif; text-align:center;'>Nyayu Chika M</h5>" ,unsafe_allow_html=True)
    st.markdown("<p style='font-family:sans-serif; text-align:center;'>Jupyter XXI</p>" ,unsafe_allow_html=True)
    st.markdown("<p style='font-family:sans-serif; text-align:center; line-height:20px;'><i>Universitas Sriwijaya</i></p>", unsafe_allow_html=True)
    mention(
      label="@nyayuchika",
      url="https://ig.me/m/nyayuchika",
    )
  with col3:
    st.image(Image.open("team/1.png"), use_column_width=True)
    st.markdown("<h5 style='font-family:sans-serif; text-align:center;'>Halomoan Filipus S</h5>" ,unsafe_allow_html=True)
    st.markdown("<p style='font-family:sans-serif; text-align:center;'>Jupyter XXI</p>" ,unsafe_allow_html=True)
    st.markdown("<p style='font-family:sans-serif; text-align:center; line-height:20px;'><i>Universitas Telkom</i></p>", unsafe_allow_html=True)
    mention(
      label="@moan.fs",
      url="https://ig.me/m/moan.fs",
    )
  with col4:
    st.image(Image.open("team/4.png"), use_column_width=True)
    st.markdown("<h5 style='font-family:sans-serif; text-align:center;'>Sukma Imelda</h5>" ,unsafe_allow_html=True)
    st.markdown("<p style='font-family:sans-serif; text-align:center;'>Cordoba</p>" ,unsafe_allow_html=True)
    st.markdown("<p style='font-family:sans-serif; text-align:center; line-height:20px;'><i>Universitas Merdeka Malang</i></p>", unsafe_allow_html=True)
    mention(
      label="@imld19_",
      url="https://ig.me/m/imld19_",
    )
  with col5:
    st.image(Image.open("team/5.png"), use_column_width=True)
    st.markdown("<h5 style='font-family:sans-serif; text-align:center;'>Wella Novita A</h5>" ,unsafe_allow_html=True)
    st.markdown("<p style='font-family:sans-serif; text-align:center;'>Cordoba</p>" ,unsafe_allow_html=True)
    st.markdown("<p style='font-family:sans-serif; text-align:center; line-height:20px;'><i>Universitas Internasional Semen Indonesia</i></p>", unsafe_allow_html=True)
    mention(
      label="@wellanvtadr",
      url="https://ig.me/m/wellanvtadr",
    )
  st.write(" ")
  st.write(" ")
  st.write(" ")
  st.write(" ")
  st.write(" ")
