<?php
$pythonExecutable = 'C:\Users\Bhoomika\AppData\Local\Programs\Python\Python310\python.exe'; // Replace with the actual path to python.exe
$pythonScriptPath = 'dynamic.py'; 
$command = "$pythonExecutable $pythonScriptPath 2>&1";
$result = exec($command);
echo "Python script output: <pre>$result</pre>";
?>
<html lang="en">
    <head>
  </head>
  <style>
	body
		{
			background-color:black;
		}
  </style>
  <body>
	   <marquee>
						 
						<?php
									$files = scandir('output/');
									$cnt1= count($files)-2;
									
									foreach($files as $file) {
										if($file !== "." && $file !== "..") {
										 echo " <img src='output/$file' width=70% height=500 >";
		
													}
									}
								 
						?>
						</div>
						  </center>
						  
						  </marquee>
					
                     
    </body>
</html>
