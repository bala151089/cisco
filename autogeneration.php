<?php

function macgen(){
			$adress = "01";
			for ($i=0;$i<5;$i++) {
				$oct = strtoupper(dechex(mt_rand(0,255)));
				strlen($oct)<2 ? $adress .= ":0$oct" : $adress .= ":$oct"; 
			}
			return $adress;
		}
function generaterandom($n){
	$mysqli = new mysqli("localhost","root","bala","cisco");

	if ($mysqli -> connect_errno) {
		echo "Failed to connect to MySQL: " . $mysqli -> connect_error;
		exit();
	}
	for($i=0;$i<$n;$i++){
		
		$mac = macgen();
		$randIP = mt_rand(0, 255) . "." . mt_rand(0, 255) . "." . mt_rand(0, 255) . "." . mt_rand(0, 255);
		#echo $randIP.PHP_EOL;
		$uniqid =  uniqid();
		$mysqli -> query("INSERT INTO router (sapid,macAddress, ipAddress,	creator_id) VALUES ('$uniqid', '$mac', '$randIP',1)");
		echo "INSERT INTO router (sapid,macAddress, ipAddress) VALUES ('$uniqid', '$mac', '$randIP')".PHP_EOL;
		$id =  $mysqli -> insert_id;
		$mysqli -> query("update router set hostname='www.example$id.com' where id=$id ");
		echo "update router set hostname='www.example$id.com' where id=$id ".PHP_EOL;
	}



$mysqli -> close();
}

generaterandom(10)
?>