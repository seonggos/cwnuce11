<?php
	$output = exec("C:/Bitnami/wampstack-5.4.40-0/apache2/htdocs/total_program/venv/Scripts/python drawingAnalyze.py 2>&1", $output2);
	print_r(error_get_last());

	echo $output;

?>
