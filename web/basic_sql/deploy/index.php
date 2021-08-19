<html>
    <head>
    <title>Basic_sqlinection</title>
    </head>

    <body>
    <h1>Find Flag!</h1>
    <form action = "index.php" method="post">
    ID : <input type="text" name="userid" />
    PW : <input type="text" name="password" />
    <input type="submit" />
    </form>
</html>

<?php

    #error_reporting(E_ALL);
    #ini_set("display_errors", 1);

    $id = $_POST['userid'];
    $pw = $_POST['password'];
	
    //start filtering

    $pw = str_replace("flag", "", $pw);
    $pw = str_replace(" ", "", $pw);

    $sql = "SELECT id FROM login_table where id = '$id' and pw = '$pw'"; 

    echo $sql."<br><br><br>";

    $conn = mysqli_connect("192.168.0.139","kuality","kuality","basic_sql");
    if (!$conn) {
	    die("Connection failed: " . mysql_connect_error());
    }

    
    $result = mysqli_query($conn,$sql) or die(mysql_error($conn));
    echo "<h1>Hello&nbsp";
    while ($row=mysqli_fetch_row($result))
    {
       #printf ("%s  %s",$row[0],$row[1]);
        echo "&nbsp$row[0]";
        echo "&nbsp$row[1]";
        echo "</h1><br>";
    }

    mysqli_close($conn);
?>
