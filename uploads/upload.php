<?php
$targetDirectory = "selected/";

$imageFields = array(
    "backgroundImage",
    "plantImage",
    "wallDecorImage",
    "sofaImage",
    "tablesImage",
    "lampImage"
);

if(isset($_POST["submit"])) {
    $uploadOk = 1;
    $allowedExtensions = array("jpg", "jpeg", "png", "gif");
    
    foreach ($imageFields as $fieldName) {
        $targetFile = $targetDirectory . basename($_FILES[$fieldName]["name"]);
        $imageFileType = strtolower(pathinfo($targetFile, PATHINFO_EXTENSION));
        
        if (file_exists($targetFile)) {
            echo "Sorry, file already exists: " . basename($_FILES[$fieldName]["name"]) . "<br>";
            $uploadOk = 0;
        }
        
        if ($_FILES[$fieldName]["size"] > 500000) {
            echo "Sorry, your file is too large: " . basename($_FILES[$fieldName]["name"]) . "<br>";
            $uploadOk = 0;
        }
        
        if (!in_array($imageFileType, $allowedExtensions)) {
            echo "Sorry, only JPG, JPEG, PNG & GIF files are allowed: " . basename($_FILES[$fieldName]["name"]) . "<br>";
            $uploadOk = 0;
        }
        
        if ($uploadOk == 0) {
            echo "Sorry, your file was not uploaded: " . basename($_FILES[$fieldName]["name"]) . "<br>";
        } else {
            if (move_uploaded_file($_FILES[$fieldName]["tmp_name"], $targetFile)) {
                echo "The file " . basename($_FILES[$fieldName]["name"]) . " has been uploaded.<br>";
            } else {
                echo "Sorry, there was an error uploading your file: " . basename($_FILES[$fieldName]["name"]) . "<br>";
            }
        }
    }
}

$pythonExecutable1 = 'C:\Users\Bhoomika\AppData\Local\Programs\Python\Python310\python.exe'; // Replace with the actual path to python.exe
$pythonScriptPath1 = 'user.py'; 
$command1 = "$pythonExecutable1 $pythonScriptPath1 2>&1";
$result1 = exec($command1);
echo "Python script output: <pre>$result1</pre>";
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
									$files = scandir('selected/useroutput/');
									$cnt1= count($files)-2;
									
									foreach($files as $file) {
										if($file !== "." && $file !== "..") {
										 echo " <img src='selected/useroutput/$file' width=70% height=500 >";
		
													}
									}
								 
						?>
						</div>
						 </center>
						  
						 </marquee>
					
                     
    </body>
</html>

