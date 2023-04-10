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
st.title("Home")

# #CSS File
# #Vendor CSS
# with open("assets/vendor/aos/aos.css") as css1:
#     vendorcss1 = css1.read()

# with open("assets/vendor/bootstrap/css/bootstrap.min.css") as css2:
#     vendorcss2 = css2.read()

# with open("assets/vendor/bootstrap-icons/bootstrap-icons.css") as css3:
#     vendorcss3 = css3.read()

# with open("assets/vendor/glightbox/css/glightbox.min.css") as css4:
#     vendorcss4 = css4.read()

# with open("assets/vendor/remixicon/remixicon.css") as css5:
#     vendorcss5 = css5.read()

# with open("assets/vendor/swiper/swiper-bundle.min.css") as css6:
#     vendorcss6 = css6.read()

# #Main CSS
# with open("assets/css/style.css") as maincss:
#     main_css = maincss.read()

# #JS File
# #Vendor JS
# with open("assets/vendor/purecounter/purecounter_vanilla.js") as js1:
#     vendorjs1 = js1.read()

# with open("assets/vendor/aos/aos.js") as js2:
#     vendorjs2 = js2.read()

# with open("assets/vendor/bootstrap/js/bootstrap.bundle.min.js") as js3:
#     vendorjs3 = js3.read()

# with open("assets/vendor/glightbox/js/glightbox.min.js") as js4:
#     vendorjs4 = js4.read()

# with open("assets/vendor/isotope-layout/isotope.pkgd.min.js") as js5:
#     vendorjs5 = js5.read()

# with open("assets/vendor/swiper/swiper-bundle.min.js") as js6:
#     vendorjs6 = js6.read()

# with open("assets/vendor/php-email-form/validate.js") as js7:
#     vendorjs7 = js7.read()

# #Main JS
# with open("assets/js/main.js") as mainjs:
#     main_js = mainjs.read()

# #HTML
# com.html("""

# <style>
#     {vendorcss1}
#     {vendorcss2}
#     {vendorcss3}
#     {vendorcss4}
#     {vendorcss5}
#     {vendorcss6}
#     {main_css}
#     {vendorjs1}
#     {vendorjs2}
#     {vendorjs3}
#     {vendorjs4}
#     {vendorjs5}
#     {vendorjs6}
#     {vendorjs7}
#     {main_js}
# </style>

# <head>
#     <meta charset="utf-8">
#     <meta content="width=device-width, initial-scale=1.0" name="viewport">

#     <title>Cake Finder</title>
#     <meta content="" name="description">

#     <meta content="" name="keywords">

#     <!-- Favicons -->
#     <link href="assets/img/favicon.png" rel="icon">
#     <link href="assets/img/apple-touch-icon.png" rel="apple-touch-icon">

#     <!-- Google Fonts -->
#     <link href="https://fonts.googleapis.com/css?family=Open+Sans:300,300i,400,400i,600,600i,700,700i|Nunito:300,300i,400,400i,600,600i,700,700i|Poppins:300,300i,400,400i,500,500i,600,600i,700,700i" rel="stylesheet">

#     <!-- =======================================================
#     * Template Name: FlexStart - v1.12.0
#     * Template URL: https://bootstrapmade.com/flexstart-bootstrap-startup-template/
#     * Author: BootstrapMade.com
#     * License: https://bootstrapmade.com/license/
#     ======================================================== -->
# </head>

# <body>
#   <!-- ======= Header ======= -->
#   <header id="header" class="header fixed-top">
#     <div class="container-fluid container-xl d-flex align-items-center justify-content-between">

#       <a href="index.php" class="logo d-flex align-items-center">
#         <img src="assets/img/logo.png" alt="">
#         <span>Cake Finder</span>
#       </a>

#       <nav id="navbar" class="navbar">
#         <ul>
#           <li><a class="nav-link scrollto active" href="#hero">Home</a></li>
#           <li><a class="nav-link scrollto" href="#about">About</a></li>
#           <li><a class="nav-link scrollto" href="#team">Team</a></li>
#           <li><a href="blog.php" class="getstarted scrollto">Let's Try!</a></li>
#         </ul>
#         <i class="bi bi-list mobile-nav-toggle"></i>
#       </nav><!-- .navbar -->

#     </div>
#   </header><!-- End Header -->
#     <!-- ======= Team Section ======= -->
#     <section id="team" class="team">

#       <div class="container" data-aos="fade-up" align="center">

#         <header class="section-header">
#           <h2>Team</h2>
#           <p>Our hard working team</p>
#         </header>

#         <div class="row gy-4">

#           <div class="col-lg-2 col-md-6=5 d-flex align-items-stretch" data-aos="fade-up" data-aos-delay="100">
#             <div class="member">
#               <div class="member-img">
#                 <img src="assets/img/team/team-1.jpg" class="img-fluid" alt="">
#                 <div class="social">
#                   <a href="https://www.instagram.com/athiyashinta.w/"><i class="bi bi-instagram"></i></a>
#                   <a href=""><i class="bi bi-linkedin"></i></a>
#                 </div>
#               </div>
#               <div class="member-info">
#                 <h4>Athiya Shinta Wulandari</h4>
# 				<span>Cordoba</span>
#                 <p>Universitas Muhammadiyah Surabaya</p></div>
#             </div>
#           </div>

#           <div class="col-lg-2 col-md-5 d-flex align-items-stretch" data-aos="fade-up" data-aos-delay="200">
#             <div class="member">
#               <div class="member-img">
#                 <img src="assets/img/team/team-2.jpg" class="img-fluid" alt="">
#                 <div class="social">
#                   <a href="https://www.instagram.com/nyayuchika/"><i class="bi bi-instagram"></i></a>
#                   <a href=""><i class="bi bi-linkedin"></i></a>
#                 </div>
#               </div>
#               <div class="member-info">
#                 <h4>Nyayu Chika Marselina</h4>
# 				<span>Jupyter XXI</span>
#                 <p>Universitas Sriwijaya</p>
# 				</div>
#             </div>
#           </div>

#           <div class="col-lg-2 col-md-5 d-flex align-items-stretch" data-aos="fade-up" data-aos-delay="300">
#             <div class="member">
#               <div class="member-img">
#                 <img src="assets/img/team/team-3.jpg" class="img-fluid" alt="">
#                 <div class="social">
#                   <a href="https://www.instagram.com/moan.fs/"><i class="bi bi-instagram"></i></a>
#                   <a href=""><i class="bi bi-linkedin"></i></a>
#                 </div>
#               </div>
#               <div class="member-info">
#                 <h4>Halomoan Filipus Simarmata</h4>
# 				<span>Jupyter XXI</span>
#                 <p>Universitas Telkom</p>
# 				</div>
#             </div>
#           </div>
		  
# 		  <div class="col-lg-2 col-md-5 d-flex align-items-stretch" data-aos="fade-up" data-aos-delay="300">
#             <div class="member">
#               <div class="member-img">
#                 <img src="assets/img/team/team-3.jpg" class="img-fluid" alt="">
#                 <div class="social">
#                   <a href="https://www.instagram.com/moan.fs/"><i class="bi bi-instagram"></i></a>
#                   <a href=""><i class="bi bi-linkedin"></i></a>
#                 </div>
#               </div>
#               <div class="member-info">
#                 <h4>Cake Finder</h4>
# 				<span>Studi Independen Batch 2</span>
#                 <p>Kampus Merdeka</p>
# 				</div>
#             </div>
#           </div>

#           <div class="col-lg-2 col-md-5 d-flex align-items-stretch" data-aos="fade-up" data-aos-delay="400">
#             <div class="member">
#               <div class="member-img">
#                 <img src="assets/img/team/team-4.jpg" class="img-fluid" alt="">
#                 <div class="social">
#                   <a href="https://www.instagram.com/imld19_/"><i class="bi bi-instagram"></i></a>
#                   <a href=""><i class="bi bi-linkedin"></i></a>
#                 </div>
#               </div>
#               <div class="member-info">
#                 <h4>Sukma Imelda</h4>
# 				<span>Cordoba</span>
#                 <p>Universitas Merdeka Malang</p>
# 				</div>
#             </div>
#           </div>
		  
# 		<div class="col-lg-2 col-md-5 d-flex align-items-stretch" data-aos="fade-up" data-aos-delay="400">
#             <div class="member">
#               <div class="member-img">
#                 <img src="assets/img/team/team-4.jpg" class="img-fluid" alt="">
#                 <div class="social">
#                   <a href="https://www.instagram.com/wellanvtadr/"><i class="bi bi-instagram"></i></a>
#                   <a href=""><i class="bi bi-linkedin"></i></a>
#                 </div>
#               </div>
#               <div class="member-info">
#                 <h4>Wella Novita Andriani</h4>
# 				<span>Cordoba</span>
#                 <p>Universitas Internasional Semen Indonesia</p>
#               </div>
#             </div>
#           </div>

#         </div>

#       </div>

#     </section><!-- End Team Section -->

#     <!-- ======= Clients Section ======= -->
#     <section id="clients" class="clients">

#       <div class="container" data-aos="fade-up">

#         <header class="section-header">
#           <h2>Our Clients</h2>
#         </header>

#         <div class="clients-slider swiper">
#           <div class="swiper-wrapper align-items-center">
#             <div class="swiper-slide"><img src="assets/img/clients/client-1.png" class="img-fluid" alt=""></div>
#             <div class="swiper-slide"><img src="assets/img/clients/client-2.png" class="img-fluid" alt=""></div>
#             <div class="swiper-slide"><img src="assets/img/clients/client-3.png" class="img-fluid" alt=""></div>
#             <div class="swiper-slide"><img src="assets/img/clients/client-4.png" class="img-fluid" alt=""></div>
#             <div class="swiper-slide"><img src="assets/img/clients/client-5.png" class="img-fluid" alt=""></div>
#             <div class="swiper-slide"><img src="assets/img/clients/client-6.webp" class="img-fluid" alt=""></div>
#             <div class="swiper-slide"><img src="assets/img/clients/client-7.png" class="img-fluid" alt=""></div>
#             <div class="swiper-slide"><img src="assets/img/clients/client-8.png" class="img-fluid" alt=""></div>
#             <div class="swiper-slide"><img src="assets/img/clients/client-9.png" class="img-fluid" alt=""></div>
#           </div>
#           <div class="swiper-pagination"></div>
#         </div>
#       </div>

#     </section><!-- End Clients Section -->


#   <!-- ======= Footer ======= -->
#   <footer id="footer" class="footer">

#     <div class="container">
#       <div class="copyright">
#         &copy; Copyright <strong><span>FlexStart</span></strong>. All Rights Reserved
#       </div>
#       <div class="credits">
#         <!-- All the links in the footer should remain intact. -->
#         <!-- You can delete the links only if you purchased the pro version. -->
#         <!-- Licensing information: https://bootstrapmade.com/license/ -->
#         <!-- Purchase the pro version with working PHP/AJAX contact form: https://bootstrapmade.com/flexstart-bootstrap-startup-template/ -->
#         Designed by <a href="https://bootstrapmade.com/">BootstrapMade</a>
#       </div>
#     </div>
#   </footer><!-- End Footer -->

#   <a href="#" class="back-to-top d-flex align-items-center justify-content-center"><i class="bi bi-arrow-up-short"></i></a>
# </body>
# """)