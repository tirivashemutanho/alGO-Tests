<?php
// Database connection
$conn = mysqli_connect("localhost", "root", "", "dbmufaro");

// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

// Fetch all records from the products/services table
$sql = "SELECT * FROM products_services";
$result = mysqli_query($conn, $sql);

// Check if query executed successfully
if ($result) {
    // Check if any records exist
    if (mysqli_num_rows($result) > 0) {
        ?>

        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Products and Services</title>
            <!-- Bootstrap CSS -->
            <link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
            <style>
                body {
                    background-color: #f8f9fa;
                }
                .container {
                    margin-top: 50px;
                }
                .card {
                    margin-bottom: 20px;
                }
            </style>
        </head>
        <body>

        <div class="container">
            <h2 class="mb-4">Products and Services</h2>
            <div class="row">
                <?php
                // Loop through each record and display as a card
                while ($row = mysqli_fetch_assoc($result)) {
                    ?>
                    <div class="col-md-4">
                        <div class="card">
                            <img class="card-img-top" src="<?php echo $row['image']; ?>" alt="Product Image">
                            <div class="card-body">
                                <h5 class="card-title"><?php echo $row['name']; ?></h5>
                                <p class="card-text"><?php echo $row['description']; ?></p>
                                <p class="card-text">Price: <?php echo $row['price']; ?></p>
                                <p class="card-text">Availability: <?php echo $row['availability_status']; ?></p>
                                <!-- Removed the edit and delete buttons -->
                                <!-- Add other fields as necessary -->
                            </div>
                        </div>
                    </div>
                    <?php
                }
                ?>
            </div>
        </div>

        </body>
        </html>

        <?php
    } else {
        // If no records found
        echo "No products or services available.";
    }
} else {
    // If query failed
    echo "Error: " . mysqli_error($conn);
}

// Close database connection
mysqli_close($conn);
?>
