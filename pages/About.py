import streamlit as st
import streamlit.components.v1 as com
from PIL import Image

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
st.title("About")

img1 = st.image("1.png")
with st.container():
  com.html("""
  <style>
  body{
    margin: 0;
    padding: 0;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    background: #23E3C9;
  }

  .slider{
    width: 800px;
    height: 500px;
    border-radius: 10px;
    overflow: hidden;
  }

  .slides{
    width: 500%;
    height: 500px;
    display: flex;
  }

  .slides input{
    display: none;
  }

  .slide{
    width: 20%;
    transition: 2s;
  }

  .slide img{
    width: 800px;
    height: 500px;
  }

  /*css for manual slide navigation*/

  .navigation-manual{
    position: absolute;
    width: 800px;
    margin-top: -40px;
    display: flex;
    justify-content: center;
  }

  .manual-btn{
    border: 2px solid #40D3DC;
    padding: 5px;
    border-radius: 10px;
    cursor: pointer;
    transition: 1s;
  }

  .manual-btn:not(:last-child){
    margin-right: 40px;
  }

  .manual-btn:hover{
    background: #40D3DC;
  }

  #radio1:checked ~ .first{
    margin-left: 0;
  }

  #radio2:checked ~ .first{
    margin-left: -20%;
  }

  #radio3:checked ~ .first{
    margin-left: -40%;
  }

  #radio4:checked ~ .first{
    margin-left: -60%;
  }

  /*css for automatic navigation*/

  .navigation-auto{
    position: absolute;
    display: flex;
    width: 800px;
    justify-content: center;
    margin-top: 460px;
  }

  .navigation-auto div{
    border: 2px solid #40D3DC;
    padding: 5px;
    border-radius: 10px;
    transition: 1s;
  }

  .navigation-auto div:not(:last-child){
    margin-right: 40px;
  }

  #radio1:checked ~ .navigation-auto .auto-btn1{
    background: #40D3DC;
  }

  #radio2:checked ~ .navigation-auto .auto-btn2{
    background: #40D3DC;
  }

  #radio3:checked ~ .navigation-auto .auto-btn3{
    background: #40D3DC;
  }

  #radio4:checked ~ .navigation-auto .auto-btn4{
    background: #40D3DC;
  }
      
  </style>
  <body>
    <!--image slider start-->
    <div class="slider">
      <div class="slides">
        <!--radio buttons start-->
        <input type="radio" name="radio-btn" id="radio1">
        <input type="radio" name="radio-btn" id="radio2">
        <input type="radio" name="radio-btn" id="radio3">
        <input type="radio" name="radio-btn" id="radio4">
        <!--radio buttons end-->
        <!--slide images start-->
        <div class="slide first">
          {img1}
        </div>
        <div class="slide">
          <img src="client-2.png" alt="">
        </div>
        <div class="slide">
          <img src="client-3.png" alt="">
        </div>
        <div class="slide">
          <img src="client-4.png" alt="">
        </div>
        <!--slide images end-->
        <!--automatic navigation start-->
        <div class="navigation-auto">
          <div class="auto-btn1"></div>
          <div class="auto-btn2"></div>
          <div class="auto-btn3"></div>
          <div class="auto-btn4"></div>
        </div>
        <!--automatic navigation end-->
      </div>
      <!--manual navigation start-->
      <div class="navigation-manual">
        <label for="radio1" class="manual-btn"></label>
        <label for="radio2" class="manual-btn"></label>
        <label for="radio3" class="manual-btn"></label>
        <label for="radio4" class="manual-btn"></label>
      </div>
      <!--manual navigation end-->
    </div>
    <!--image slider end-->

    <script type="text/javascript">
    var counter = 1;
    setInterval(function(){
      document.getElementById('radio' + counter).checked = true;
      counter++;
      if(counter > 4){
        counter = 1;
      }
    }, 5000);
    </script>

  </body>

      
  """, height=500)