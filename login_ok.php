<meta charset="uff-8"/>
<?php
	$conn = mysqli_connect(
		"localhost",
		"hoyoung",
		"Hoyoung123!",
		"opentutorials"
	);

	if($_POST["userid"] == "" || $_POST["userpw"] == "") {
		echo "<script>alert('아이디나 패스워드를 입력하세요'); history.back();</script>";
	} else {
		$password = $_POST["userpw"];
		$sql = "SELECT * FROM member WHERE id='{$_POST['userid']}'";
		$result = mysqli_query($conn, $sql);
		$member = mysqli_fetch_array($result);
		$hash_pw = $member["pw"];
		
		if(password_verify($password, $hash_pw)) {
			session_start();
			$_SESSION["userid"] = $member["id"];
			$_SESSION["userpw"] = $member["pw"];
			echo "<script>alert('로그인 되었습니다.'); location.href='./index.php';</script>";
		} else {
			echo "<script>alert('아이디 혹은 비밀번호를 확인하세요.'); history.back();</script>";
		}
	}
?>
