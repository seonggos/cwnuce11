<!DOCTYPE html>
<html>
    <head>
        <title>그림일기 분석 프로젝트 | About</title>
        <meta name="description" content="This is the description">
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
        </header>

        <section class="container content-section">
			<h2 class="section-header">TEST</h2>
      		<img src="Images/test_drawing.png" style="width: 720px; margin-bottom: 30px;">
      		<p>그림일기를 분석하려면 그림일기를 촬영해서 이미지를 업로드 해주세요. 업로드만으로 빠르게 결과를 알려줍니다.</p>
      		<p>To analyze the picture diary, please take a picture diary and upload the image. Upload results quickly. Google translated.</p>
			<span class="filebox">
				<form enctype="multipart/form-data" action="upload_ok.php" method="post">
					<label class="btn-primary upload-btn" for="ex_file">그림 선택</label>
					<input type="file" name="myfile[]" multiple="multiple" id="ex_file">
					<input class="upload-btn btn-primary" type="submit" value="그림 업로드">
				<button class="upload-btn btn-primary" onclick="location.href='./result_exec.php'">결과 보기</button>
			</span>
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
