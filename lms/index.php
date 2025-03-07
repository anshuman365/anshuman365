<?php
require '../includes/config.php';
$query = "SELECT * FROM courses";
$result = $conn->query($query);
?>
<!DOCTYPE html>
<html>
<head><title>Courses</title></head>
<body>
<h2>Available Courses</h2>
<?php while ($row = $result->fetch_assoc()): ?>
    <div>
        <h3><?php echo $row['title']; ?></h3>
        <p><?php echo $row['description']; ?></p>
        <p>₹<?php echo $row['price']; ?></p>
        <a href="enroll.php?id=<?php echo $row['id']; ?>">Enroll Now</a>
    </div>
<?php endwhile; ?>
</body>
</html>