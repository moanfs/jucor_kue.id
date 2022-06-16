<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />

    <!-- css -->
    <link rel="stylesheet" href="vendor/css/style.css" />
    <link rel="stylesheet" href="vendor/bootstrap/css/bootstrap.min.css">

    <title>Cake Finder</title>
</head>

<body>
    <!-- navbar -->
    <div id="rc_logo">
        <a href="#home" title="Logo">Cake Finder</a>
    </div>
    <div class="rc_nav" id="centered_nav">
        <a href="#home" class="logo2" title="Home"><img src="vendor/img/logo.png" width="100px" alt=""></a>
        <!-- <a href="#home" class="logo2" title="Home">Cake Finder</a> -->
        <a href="#services" title="Services">Cake</a>
        <a href="#about" title="About">About Us</a>
        <a href="javascript:void(0);" title="Menu" style="font-size:18px;" class="icon" onclick="myFunction()">&#9776;</a>
    </div>
    <!-- end navbar -->


    <!-- get started -->
    <section class="section mt-5">
        <div class="container">
            <div class="d-flex justify-content-center">
                <div class="col col-lg-8 col-md-8 text-center">
                    <h2>Find Your Cake!!</h2>
                    <p>Aplikasi <i>Cake Finder</i> ini dapat membantu anda mencari tau nama kue yang ada di indonesia dengan cara, anda dapat mengunggah gambar kue atau dengan cara menyalakan kamera yang ada pada perangkat anda. aplikasi ini menggunakan pembelajaran mesin yang akan menghasilkan keluaran berupa hasil dari unggahan anda dan mengklasifikasikan jenis kue tersebut. Pada aplikasi ini hanya dapat mengklasifikasikan 8 jenis kue yang ada di Indonesia, antaranya <b>Kue Klepon, Kue Lumpur, Kue Kastengel, Kue Putri Salju, Kue Serabi, Kue Dadar Gulung, Kue Lapis, dan Kue Risoles</b></p>
                    <div class="getstarted">
                        <a href="find.php" class="btn btn-danger">Get Started</a>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!-- end get started -->

    <!-- content -->
    <section class="section mt-5">
        <div class="container">
            <div class="">
                <h3 class="text center">Jenis Kue Tradisional</h3>
                <div class="d-flex justify-content-center">
                    <div class="col-sm-3 m-3">
                        <div class="card">
                            <img src="vendor/img/dadargulung1.jpg" class="card-img-top" alt="...">
                            <div class="card-body">
                                <h5 class="card-title">Kue Dadar Gulung</h5>
                                <p class="card-text">Kue dadar gulung dapat digolongkan sebagai panekuk yang diisi dengan parutan kelapa yang dicampur dengan gula jawa cair. Kulit dadar gulung identik dengan warna hijau karena diberi pewarna daun suji.</p>
                            </div>
                        </div>
                    </div>
                    <div class="col-sm-3 m-3">
                        <div class="card">
                            <img src="vendor/img/klepon1.png" class="card-img-top" alt="...">
                            <div class="card-body">
                                <h5 class="card-title">Kue Kelepon</h5>
                                <p class="card-text">Klepon adalah makanan tradisional Indonesia yang termasuk ke dalam kelompok jajanan pasar. Klepon terbuat dari tepung beras ketan yang dibentuk seperti bola-bola kecil dan diisi dengan gula merah lalu direbus.</p>
                            </div>
                        </div>
                    </div>
                    <div class="col-sm-3 m-3">
                        <div class="card">
                            <img src="vendor/img/risoles1.png" class="card-img-top" alt="...">
                            <div class="card-body">
                                <h5 class="card-title">Risoles</h5>
                                <p class="card-text">Risoles adalah pastri berisi daging, biasanya daging cincang, dan sayuran yang dibungkus dadar, dan digoreng setelah dilapisi tepung panir dan kocokan telur ayam. Hidangan ini juga dapat dipanggang di dalam oven, dan disajikan sebagai makanan ringan.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!-- end content -->

    <!-- about us -->
    <section class="section mt-5">
        <div class="container">
            <h3 class="text center">About Us</h3>

        </div>
    </section>
    <!-- end about us -->

    <script>
        function myFunction() {
            var x = document.getElementById("centered_nav");
            if (x.className === "rc_nav") {
                x.className += " responsive";
            } else {
                x.className = "rc_nav";
            }
        }
    </script>
</body>

</html>