<?php
require '../includes/config.php';
$query = "SELECT * FROM products";
$result = $conn->query($query);
?>
<!DOCTYPE html>
<html>
<head><title>Shop</title></head>
<body>
<h2>Products</h2>
<?php while ($row = $result->fetch_assoc()): ?>
    <div>
        <h3><?php echo $row['name']; ?></h3>
        <p><?php echo $row['description']; ?></p>
        <p>₹<?php echo $row['price']; ?></p>
        <a href="cart.php?id=<?php echo $row['id']; ?>">Add to Cart</a>
    </div>
<?php endwhile; ?>
</body>
</html>