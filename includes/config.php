<?php
$host = "dpg-cv57qsjtq21c73f28e10-a.oregon-postgres.render.com"; // External hostname from Render
$port = "5432";
$dbname = "ecommerce_lms";
$user = "ecommerce_lms_user";
$password = "n1u18mmCtaeMdVTVKhgiNm0urf195dL5";

try {
    $dsn = "pgsql:host=$host;port=$port;dbname=$dbname;";
    $conn = new PDO($dsn, $user, $password, [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION]);
    echo "Connected to PostgreSQL successfully!";
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}
?>