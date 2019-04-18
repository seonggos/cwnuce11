<html>
<head>
	<title>그림일기 분석 프로젝트</title>
	<meta name="description" content="Tis is the description">
	<meta charset="utf-8">
	<link rel="stylesheet" href="styles.css">
</head>
<body>
	<header class="main-header">
		<nav class="nav main-nav">
			<ul>
				<li><a href="index.php">HOME</a></li>
				<li><a href="test.php">TEST</a></li>
				<?php
					session_start();
				if(isset($_SESSION["userid"])) {
						//echo "<h2>{$_SESSION['userid']}님 환영합니다.</h2>";
						echo "<li><a href='logout.php'>LOGOUT</a></li>";
					} else {
						echo "<li><a href='login.html'>LOGIN</a></li>";
					}
				?>
			</ul>
		</nav>
		<h1 class="title">그림일기 분석 프로젝트</h1>
		<div class="container">
			<button class="btn btn-header" type="button" onclick="location.href='test.php'">분석하러 가기</button>
		</div>
	</header>
	<section class="content-section container">
			<h2 class="section-header">ABOUT</h2>
			<img class="about-band-image" src="Images/index_drawing.jpg">
			<p>유아의 그림일기에는 작성자의 일상과 감정이 고스란히 담긴다. 때문에 이 작품을 분석하는 것은 작성자의 심리상태를 진단하는 데 큰 도움이 될 수 있다. 이 프로그램은 초등학생의 그림일기를 바탕으로 딥러닝 기법을 이용해 그림을 분석, 정신적으로 불안정하거나 도움이 필요한 아이를 분류해내는 것을 목표로 한다. 결과적으로 프로그램을 통해 발견된 아이는 심리상담 전문가에게 연결되어 치료를 받을 수 있도록 도울 수 있다.</p><br>
			<p>In the picture diary of the children, the essence and the emotion of the writer are intact. Diagnosing the author's psychological state is a great help. This program analyzes elementary school students' pictures and helps to classify them based on scientific evidence. As a result, when the program was found, the connection was broken when it was disconnected. Google translated.</p>
			<br><br>
	</section>
	<footer class="main-footer">
		<div class="container main-footer-container">
			<h3 class="team-name">Team Cocacola</h3>
			<ul class="nav footer-nav">
				<li>
					<a href="mailto:yveltal@naver.com" target="_blank">
						<img src="Images/email_white.png">
					</a>
				</li>
			</ul>
		</div>
	</footer>
</body>
</html>
