<?php
session_start();
if ($_SESSION['logged'] != 1) header('Location: /login.php');
?>
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="">
    <meta name="author" content="">
    <!--<link rel="icon" href="../../favicon.ico"> -->

    <title>LOG EVENTS</title>

    <!-- Bootstrap core CSS -->
    <link href="css/bootstrap.min.css" rel="stylesheet">



    <!-- Custom styles for this template -->
    <link href="signin.css" rel="stylesheet">


  </head>

  <body>

    <div class="container">

      <h2>Log Events</h2>
	  
	  <table class="table table-striped">
		<thead>
		  <tr>
			<th>ID #</th>
			<th>Timestamp</th>
			<th>Hacker IP</th>
			<th>Page</th>
		  </tr>
		</thead>
		<tbody>
		  
			<?php
			$servername = "honeydb";
			$username = "honeypot";
			$password = "123";
			$dbname = "honeypot";

			// Create connection
			$con=mysqli_connect($servername, $username, $password, $dbname);

			// Check connection
			if (mysqli_connect_errno())
  {
  echo "Failed to connect to MySQL: " . mysqli_connect_error();
  }


			$sql = "SELECT * from log";
			$result=mysqli_query($con,$sql);

			if ($result->num_rows > 0) {
				// output data of each row
				while($row = mysqli_fetch_assoc($result)) {
					echo "<tr>";
					echo "<td>" . $row["id"] . "</td>";
					echo "<td>" . $row["date"] . "</td>";
					echo "<td>" . $row["iphacker"] . "</td>";
					echo "<td>" . $row["uri"] . "</td>";
					echo "</tr>";
				}
			} 
			else 
			{
				echo "0 results";
			}
			mysqli_close($con);
			?>
		  
		</tbody>
	  </table>

    </div> <!-- /container -->


    <script src="js/bootstrap.min.js"></script>
  </body>
</html>
