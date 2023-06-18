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

if ($auth != "AUTH") { // AUTH Check
   exit();
}
// Mysql Information

$host = "localhost";
$db = "dbname";
$user = "user";
$pass = "password";

$conn = new PDO("mysql:host=$host;dbname=$db", "$user", "$pass");
$conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$query = $conn->prepare("SELECT * FROM wp_posts WHERE ID='$id'");

$query->execute();
if ($query->rowCount() <= 0) {
    echo'<h1 class="entry-title">notfound</h1>';
    exit();
} else {
$result = $query->fetchAll();
echo'<h1 class="entry-title">'.$result[0]["post_name"].'</h1>';
$json = $result[0]["post_content"];
$jsonString = str_replace(utf8_encode("<img"),"<img id='content'",$json);

print_r ($jsonString);
}
