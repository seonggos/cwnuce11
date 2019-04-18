<?php
	$userid = $_POST["userid"];
	$userpw = password_hash($_POST["userpw"], PASSWORD_DEFAULT);
	$username = $_POST["name"];
	$adress = $_POST["adress"];
	$sex = $_POST["sex"];
	$email = $_POST["email"].'@'.$_POST["emadress"];

	$conn = mysqli_connect(
		"localhost",
		"hoyoung",
		"Hoyoung123!",
		"opentutorials"
	);

	if(mysqli_connect_error()) {
		printf("Connect failed: %s\n", mysqli_connect_error());
		printf("Error number: %d\n", mysqli_connect_errno());
		exit();
	}
	$sql = "INSERT INTO member (id, pw, name, adress, sex, email) VALUES ('{$userid}','{$userpw}','{$username}','{$adress}','{$sex}','{$email}')";
	$result = mysqli_query($conn, $sql);

	if($result === false) {
		echo mysqli_error($conn);
	}
?>

<meta charset="utf-8"/>
<script type="text/javascript">
	alert("회원가입이 완료되었습니다.");
</script>
<meta http-equiv="refresh" content="0 url=./index.php">
