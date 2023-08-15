<!DOCTYPE html>
<html>
<head>
    <title>Image Upload Form</title>
	
			<link rel="preconnect" href="https://fonts.googleapis.com">
			<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
			<link href="https://fonts.googleapis.com/css2?family=Oxygen&display=swap" rel="stylesheet">
	    
			<link rel="preconnect" href="https://fonts.googleapis.com">
			<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
			<link href="https://fonts.googleapis.com/css2?family=Play&display=swap" rel="stylesheet">
			<link rel="preconnect" href="https://fonts.googleapis.com">
			<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
			<link href="https://fonts.googleapis.com/css2?family=Labrada:wght@600&display=swap" rel="stylesheet">
			<link rel="preconnect" href="https://fonts.googleapis.com">
			<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
			<link href="https://fonts.googleapis.com/css2?family=Inter&display=swap" rel="stylesheet">
	
</head>
<style>
		h1
		{
			background-color:black;
			color:white;
			padding:15px;
			margin-left:300px;
			margin-right:300px;
					
		}
		form
		{
			background-color:#adaaa1;
			padding:30px;
			margin-left:300px;
			margin-right:300px;
		}
		body
		{
		    
			background-image:url('d.png');
			background-repeat:no-repeat;
			background-size:cover;
		}
		table,tr,td
		{
			border:3px solid #cce6ff;
			font-family:inter;
			
		}
		h1
		{
			font-family:play;
		}
		label
		{
			font-family:labrada;
		}
		#button
		{
			padding:10px;
		}
			
	</style>

<body>
    <h1 align="center">Image Upload Form</h1>
	<div align="center">
		<form action="upload.php" method="post" enctype="multipart/form-data">
			<label>Select background image:</label>
			<input type="file" name="backgroundImage" accept="image/*" />
			<br><br>
			<label>Select image of plant:</label>
			<input type="file" name="plantImage" accept="image/*" />
			<br><br>
			<label>Select image of wall decor:</label>
			<input type="file" name="wallDecorImage" accept="image/*" />
			<br><br>
			<label>Select image of sofa:</label>
			<input type="file" name="sofaImage" accept="image/*" />
			<br><br>
			<label>Select image of tables:</label>
			<input type="file" name="tablesImage" accept="image/*" />
			<br><br>
			<label>Select image of lamp:</label>
			<input type="file" name="lampImage" accept="image/*" />
			<br><br><br><br>
			<input type="submit" value="Upload Images" name="submit">
		</form>
	</div>
</body>
</html>
