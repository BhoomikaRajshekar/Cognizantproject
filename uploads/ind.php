<?php
$pythonExecutable = 'C:\Users\Bhoomika\AppData\Local\Programs\Python\Python310\python.exe'; // Replace with the actual path to python.exe
$pythonScriptPath = 'user.py'; 
$command = "$pythonExecutable $pythonScriptPath 2>&1";
$result = exec($command);
echo "Python script output: <pre>$result</pre>";
?>
<html lang="en">
    <head>
  </head>
	   <marquee>
						  
						<?php
									$files = scandir('useroutput/');
									$cnt1= count($files)-2;
									
									foreach($files as $file) {
										if($file !== "." && $file !== "..") {
										 echo " <img src='output/$file' width=50% height=300 >";
		
													}
									}
								 
						?>
						</div>
						  </center>
						  
						  </marquee>
					
                     
    </body>
</html>
