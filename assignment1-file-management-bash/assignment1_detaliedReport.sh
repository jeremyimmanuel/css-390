#CSS 390 Scripting Language
#Professor Morris Bernstein
#Assignment 1: File Management
#Jeremy Tandjung

#!/bin/bash

#DETAILED REPORT
cd Music

echo Multi-Genre Artists:
find . | grep .ogg | cut -d "/" -f 2,3 | sort | uniq | cut -d "/" -f 2 | sort | uniq -d | while read artist
do
    echo  "$artist"
   
    artistGenre="$(find . | grep "$artist" | cut -d "/" -f 2 | sort | uniq)"
    for genre in "$artistGenre"
    do
        echo " $genre"
    done
done

echo 

echo Multi-Disk Albums:
find . | grep .ogg | grep disk | cut -d "/" -f 4 | sort | uniq | while read artist
do
    echo " $artist"
    find . | grep "$artist" | grep .ogg | grep disk | cut -d "/" -f 4 | sort | uniq | while read album 
    do 
        echo "  $album"
    done
done