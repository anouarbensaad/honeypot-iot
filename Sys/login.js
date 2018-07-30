var attempt = 5; 

function validate(){

	var username = document.getElementById("username").value;

	var password = document.getElementById("password").value;



	if ( username == "topadmin" && password == "topadmin"){

		alert ("Login successfully");

		window.location = "Sys/fake/index.html"; 

		return false;

	}

	else{

		attempt --;

		alert("Be careful you have left few attempts before closing your session;");

		

		

		if( attempt == 0){

			document.getElementById("username").disabled = true;

			document.getElementById("password").disabled = true;

			document.getElementById("submit").disabled = true;

			return false;

		}

	}

}
