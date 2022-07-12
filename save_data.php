<?php
// the $_POST[] array will contain the passed in filename and data
// the directory "data" is writable by the server

$filename = "data/".$_POST['filename'];

$data = $_POST['filedata'];

// write the file to disk
//file_put_contents($filename, $current);

// Write the contents to the file, 
// using the FILE_APPEND flag to append the content to the end of the file
// and the LOCK_EX flag to prevent anyone else writing to the file at the same time
file_put_contents($filename, $data, FILE_APPEND | LOCK_EX);

?>