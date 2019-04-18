<?php
	session_start();
	session_destroy();
?>
<meta charset="utf-8">
<script>
	alert("로그아웃 되었습니다.");
	location.href="./index.php";
</script>
