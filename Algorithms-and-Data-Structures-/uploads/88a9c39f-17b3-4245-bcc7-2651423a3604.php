<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Client Registration</title>
    <!-- Bootstrap CSS -->
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background-color: #f8f9fa;
        }
        .container {
            max-width: 500px;
            margin-top: 50px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            padding: 30px;
            background-color: #fff;
        }
        .btn-primary {
            background-color: #007bff;
            border-color: #007bff;
        }
        .btn-primary:hover {
            background-color: #0069d9;
            border-color: #0062cc;
        }
    </style>
</head>
<body>

<div class="container">
    <h2 class="mb-4">Client Registration</h2>

    <?php
    // Database connection
    $conn = mysqli_connect("localhost", "root", "", "dbmufaro");

    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        // Form data validation
        $errors = [];
        $required_fields = ["first_name", "last_name", "phone_number", "email_address", "date_of_birth", "client_type", "mailing_list_option", "password"];
        foreach ($required_fields as $field) {
            if (empty($_POST[$field])) {
                $errors[] = "$field is required";
            }
        }

        // If no errors, insert data into the database
        if (empty($errors)) {
            $first_name = $_POST['first_name'];
            $last_name = $_POST['last_name'];
            $phone_number = $_POST['phone_number'];
            $email_address = $_POST['email_address'];
            $date_of_birth = $_POST['date_of_birth'];
            $client_type = $_POST['client_type'];
            $web_technologies = isset($_POST['web_technologies']) ? $_POST['web_technologies'] : "";
            $mailing_list_option = $_POST['mailing_list_option'];
            $password = md5($_POST['password']);

            // Check if email already exists
            $email_check_query = "SELECT * FROM clients WHERE email_address='$email_address' LIMIT 1";
            $result = mysqli_query($conn, $email_check_query);
            $user = mysqli_fetch_assoc($result);

            if ($user) { // If email exists
                if ($user['email_address'] === $email_address) {
                    echo '<div class="alert alert-danger">Email already exists. Please choose another email.</div>';
                }
            } else { // If email does not exist, insert data into clients table
                $sql = "INSERT INTO clients (first_name, last_name, phone_number, email_address, date_of_birth, client_type, web_technologies, mailing_list_option, password) 
                        VALUES ('$first_name', '$last_name', '$phone_number', '$email_address', '$date_of_birth', '$client_type', '$web_technologies', '$mailing_list_option', '$password')";
                if (mysqli_query($conn, $sql)) {
                    echo '<div class="alert alert-success">Registration successful. Please <a href="login.php">login</a>.</div>';
                } else {
                    echo '<div class="alert alert-danger">Error: ' . mysqli_error($conn) . '</div>';
                }
            }
        } else {
            // Display validation errors
            foreach ($errors as $error) {
                echo '<div class="alert alert-danger">' . $error . '</div>';
            }
        }
    }
    ?>

    <form method="post">
        <div class="form-group">
            <input type="text" class="form-control" placeholder="First Name" name="first_name">
        </div>
        <div class="form-group">
            <input type="text" class="form-control" placeholder="Last Name" name="last_name">
        </div>
        <div class="form-group">
            <input type="text" class="form-control" placeholder="Phone Number" name="phone_number">
        </div>
        <div class="form-group">
            <input type="email" class="form-control" placeholder="Email Address" name="email_address">
        </div>
        <div class="form-group">
            <input type="date" class="form-control" name="date_of_birth">
        </div>
        <div class="form-group">
            <select class="form-control" name="client_type">
                <option value="Admin">Admin</option>
                <option value="User">User</option>
            </select>
        </div>
        <div class="form-group">
            <input type="text" class="form-control" placeholder="Web Technologies" name="web_technologies">
        </div>
        <div class="form-check mb-3">
            <input class="form-check-input" type="checkbox" value="Yes" id="mailing_list_option" name="mailing_list_option">
            <label class="form-check-label" for="mailing_list_option">
                Subscribe to mailing list
            </label>
        </div>
        <div class="form-group">
            <input type="password" class="form-control" placeholder="Password" name="password">
        </div>
        <button type="submit" class="btn btn-primary btn-block">Register</button>
    </form>
</div>

</body>
</html>
