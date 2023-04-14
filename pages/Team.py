import streamlit as st
import streamlit.components.v1 as com

page_bg_img = """
<style>
[data-testid="stAppViewContainer"]{
  background: linear-gradient(to bottom right, #deaaff, #c0fdff);
}

[data-testid="stHeader"]{
  background-color: #5e6472;
}

[data-testid="stSidebar"]{
  background-color: #5e6472;
}

</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)
st.title("Our Team")

with st.container():
  col1, col2, col3, col4, col5 = st.columns(5)
  with col1:
    com.html("""
    <h4>Athiya Shinta Wulandari</h4>
    <span>Cordoba</span>
    <p>Universitas Muhammadiyah Surabaya</p>
    """)
  with col2:
    com.html("""
    <h4>Halomoan Filipus Simarmata</h4>
    <span>Jupyter XXI</span>
    <p>Universitas Telkom</p>
    """)
  with col3:
    com.html("""
    <h4>Nyayu Chika Marselina</h4>
    <span>Jupyter XXI</span>
    <p>Universitas Sriwijaya</p>
    """)
  with col4:
    com.html("""
    <h4>Sukma Imelda</h4>
    <span>Cordoba</span>
    <p>Universitas Merdeka Malang</p>
    """)
  with col5:
    com.html("""
    <h4>Wella Novita Andriani</h4>
    <span>Cordoba</span>
    <p>Universitas Internasional Semen Indonesia</p>
    """)
