<?php
    //include "dbcon.php";

    //$db = new mysqli($dbhost,$dbuser,$dbpassword,$dbname);

    //if($conn -> connect_error){
    //   die("connection failed: ".$conn->connect_error);
//}

//content type filtering
    function content_type($file) {
	$imageKind = array('jpeg','JPG','PNG','X-PNG','png','x-png');
	$file_type_check = explode('.',$file);
        $file_type = $file_type_check[count($file_type_check)-1];
   	 
	foreach($imageKind as $value){
	    $i=1;
	    if($file_type === $value)
		    return True;
	    else{
		if($i===count($imageKind))
			return;
		$i++;
	    }
	}
    }    

    if ($_SERVER['REQUEST_METHOD'] === 'POST'){
	$file = $_FILES['fileup'];
        $path = './upload/';
        $name = $file['name'];
	$tmp_name = $file['tmp_name'];
	$type = content_type($name);
	
	if ( $error > 0 ) {
            echo "Error: " . $error . "<br>";
        }
	else {
            if (file_exists($path/$name)) {
                echo $name . " already exists. ";
            }
	    else {
		    $res = "./upload/{$name}";
		    if(move_uploaded_file($tmp_name,"./upload/".$name)){
			    //echo "<img src='{$res}' width='100%' />";
			    echo "<a href='{$res}'>".$name."</a><br>";
		    }
		    else{
		    	echo "Something wrong in your TRY!";
		    }
            }
        }
    }
    else {
        echo "Error !";
    }
    die();

    // $file_type_check = explode('.',$name);
    // $file_type = $file_type_check[count($file_type_check)-1];
    // echo $file_type;


    //$imageKind = array('image/jpeg','image/JPG','image/PNG','image/X-PNG','image/png','image/x-png');

    

    

?>