<?php

$id = $_GET["id"];
$auth = $_GET["auth"];
if ($id == null) {
exit();}
if (empty($id)) {
    exit();
   
}
if (empty($auth)) {
 exit();
}

if ($auth != "AUTH") { // Doğrulama Kontrolü
   exit();
}
// Mysql Bilgileri
$host = "localhost";
$db = "dbname";
$user = "user";
$pass = "password";

$conn = new PDO("mysql:host=$host;dbname=$db", "$user", "$pass");
$conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$sorgu = $conn->prepare("SELECT * FROM wp_posts WHERE ID='$id'");

$sorgu->execute();
if ($sorgu->rowCount() <= 0) {
    echo'<h1 class="entry-title">notfound</h1>';
    exit();
} else {
$sonuc = $sorgu->fetchAll();
echo'<h1 class="entry-title">'.$sonuc[0]["post_name"].'</h1>';
$json = $sonuc[0]["post_content"];
$jsonString = str_replace(utf8_encode("<img"),"<img id='icerik'",$json);

print_r ($jsonString);
}
