<?php
	$save_dir = "uploads/";
	$allowed_ext = array("jpg", "jpeg", "png", "gif");

	$files = array_filter($_FILES["myfile"]["name"]);
	$total = count($_FILES["myfile"]["name"]);

	for($i = 0; $i < $total; $i++) {
		$error = $_FILES["myfile"]["error"][$i];
		$name = $_FILES["myfile"]["name"][$i];
		$ext = end(explode('.', $name));
	 
		if($error != UPLOAD_ERR_OK) {
			switch($error) {
				case UPLOAD_ERR_INI_SIZE:
				case UPLOAD_ERR_FORM_SIZE:
					echo "File size is too big. ($error)";
					break;
				case UPLOAD_ERR_NO_FILE:
					echo "Can't find this file. ($error)";
					break;
				default:
					echo "File isn't uploaded normally. ($error)";
			}

			exit;
		}

		if(!in_array($ext, $allowed_ext)) {
			echo "Invalid extension.";
			exit;
		}
		move_uploaded_file($_FILES["myfile"]["tmp_name"][$i], $save_dir.$name);
	}
	echo "<script>
			alert('파일 업로드가 정상적으로 완료되었습니다.');
			location.href='./index.php'</script>";
?>
