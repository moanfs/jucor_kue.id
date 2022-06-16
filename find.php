<?php include "koneksi.php"; ?>
<!doctype html>
<html lang="en">

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
    <link href="vendor/css/style.css" rel="stylesheet">
    <!-- <link href="vendor/css/style2.css" rel="stylesheet"> -->

    <title>Cake Finder</title>
</head>

<body>

    <!-- navbar -->
    <div id="rc_logo">
        <a href="#home" title="Logo">Cake Finder</a>
    </div>
    <div class="rc_nav" id="centered_nav">
        <a href="index.php" class="logo2" title="Home"><img src="vendor/img/logo.png" width="100px" alt=""></a>
        <!-- <a href="#home" class="logo2" title="Home">Cake Finder</a> -->
        <a href="index.php" title="Services">Cake</a>
        <a href="index.php" title="About">About Us</a>
        <a href="javascript:void(0);" title="Menu" style="font-size:18px;" class="icon" onclick="myFunction()">&#9776;</a>
    </div>
    <!-- end navbar -->


    <!-- content -->
    <section class="section mt-5">
        <div class="container-fluid">
            <div class="d-flex justify-content-center">
                <div class="col col-lg-6 col-md-6 text-center">
                    <h2>Find Your Cake!!</h2>
                    <!-- <div class="btn-group">
                        <a href="#" class="btn btn-danger">Upload</a>
                        <a href="#" class="btn btn-outline-danger">Camera</a>
                    </div> -->

                    <!-- form predict -->
                    <!-- <form action="" method="POST" enctype="multipart/form-data">
                        <div class="form">
                            <div class="grid">
                                <div class="form-element">
                                    <input type="file" id="file-1" accept="image/*">
                                    <label for="file-1" id="file-1-preview">
                                        <img src="vendor/img/contoh.jpg" alt="">
                                        <div>
                                            <span>+</span>
                                        </div>
                                    </label>
                                </div>
                            </div>
                            <div class="getstarted">
                                <input type="submit" class="btn btn-danger mt-4 ps-4 pe-4" name="findout" value="Find Out">
                            </div>
                        </div>
                    </form> -->
                    <form action="" method="POST" enctype="multipart/form-data">
                        <input type="hidden" name="">
                        <input type="file" name="nFile">
                        <input type="submit" name="nButton" value="UPLOAD">
                    </form>


                    <?php
                    // if (isset($_POST['nButton'])) {
                    //     $model = panggil_model();
                    //     echo 'Hasil prediksi:' . $model . "</br>";
                    // }
                    if (isset($_POST['nButton'])) {
                        $direktori = "berkas/";
                        $namaFile  = $_FILES['nFile']['name'];
                        move_uploaded_file($_FILES['nFile']['tmp_name'], $direktori . $namaFile);

                        mysqli_query($conn, "insert into tb_berkas set nama='$namaFile'");
                        echo "</b>berhasil di upload<br><br><br>";

                        // $model = panggil_model();
                        // echo 'Hasil prediksi:' . $model . "</br>";
                        // // $mod = $model;
                        // foreach ($models as $data => $row) {

                        //     echo "<tr><td>" . $model . "</td></tr>";
                        // }
                        // echo "</table>";
                    }
                    ?>
                    <!-- end form predict -->
                </div>
            </div>
        </div>
    </section>
    <!-- end content -->
    <!-- <script>
        function previewBeforeUpload(id) {
            document.querySelector("#" + id).addEventListener("change", function(e) {
                if (e.target.files.length == 0) {
                    return;
                }
                let file = e.target.files[0];
                let url = URL.createObjectURL(file);
                document.querySelector("#" + id + "-preview div").innerText = file.name;
                document.querySelector("#" + id + "-preview img").src = url;
            });
        }

        previewBeforeUpload("file-1");
    </script> -->
    <!-- Optional JavaScript; choose one of the two! -->

    <!-- Option 1: Bootstrap Bundle with Popper -->
    <script src="vendor/bootstrap/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
    <script src="vendor/js/script.js"></script>
    <!-- Option 2: Separate Popper and Bootstrap JS -->
    <!--
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.2/dist/umd/popper.min.js" integrity="sha384-7+zCNj/IqJ95wo16oMtfsKbZ9ccEh31eOz1HGyDuCQ6wgnyJNSYdrPa03rtR1zdB" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js" integrity="sha384-QJHtvGhmr9XOIpI6YVutG+2QOK9T+ZnN4kzFN1RtK3zEFEIsxhlmWl5/YESvpZ13" crossorigin="anonymous"></script>
    -->
</body>

</html>