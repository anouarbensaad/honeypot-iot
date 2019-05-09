<?php
session_start();
if ($_SESSION['logged'] == 1) header('Location: /index.php');
//var_dump($_POST);
$login=$_POST['inputname'];
$pass=$_POST['inputPassword'];
if ($login == 'isetadmin' && $pass == 'isetadmin')
	{
	  $_SESSION['logged']=1;
	  header('Location: /index.php');
        }

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

    <title>IsetSo Authentication</title>

   
    <link href="css/bootstrap.min.css" rel="stylesheet">



    <!-- Custom styles for this template -->
    <link href="signin.css" rel="stylesheet">


  </head>

  <body>

    <div class="container">

      <form class="form-signin" method="post">
        <h2 class="form-signin-heading">IsetSo Authentication</h2>
        <label for="inputname" class="sr-only">Username</label>
        <input type="text" name="inputname" class="form-control" placeholder="Username" required autofocus>
        <label for="inputPassword" class="sr-only">Password</label>
        <input type="password" name="inputPassword" class="form-control" placeholder="Password" required>
        <div class="checkbox">
          <label>
            <input type="checkbox" value="remember-me"> Remember me
          </label>
        </div>
<!--script language="javascript" src="login.js"></script-->
        <button class="btn btn-lg btn-primary btn-block" type="submit">Connexion</button>
	<button class="btn btn-lg btn-primary btn-block" type="reset">Annuler</button>
	
      </form>

    </div> <!-- /container -->


    <script src="js/bootstrap.min.js"></script>
  </body>
</html>
