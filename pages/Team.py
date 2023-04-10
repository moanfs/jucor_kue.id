import streamlit as st
# import streamlit.components.v1 as com

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