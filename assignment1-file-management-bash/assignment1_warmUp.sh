#CSS 390 Scripting Language
#Professor Morris Bernstein
#Assignment 1: File Management
#Jeremy Tandjung

#!/bin/bash

#WARMUP
cd Music

numTracks="$(find . | grep .ogg | cat | wc -l)"
echo Total Tracks: $numTracks
echo 

numArtist="$(find . | grep .ogg | cut -d "/" -f 3 | sort | uniq | wc -l)"
echo Total Artists: $numArtist
echo

echo Multi-Genre Artist: 
echo "$(find . | grep .ogg | cut -d "/" -f 2,3 | sort | uniq | cut -d "/" -f 2 | sort | uniq -d)"
echo

echo Multi-Disk Albums: 
echo "$(find . | grep .ogg | grep disk | cut -d "/" -f 4 | sort | uniq)"
echo

#DETAILED REPORT

# echo DETAILED REPORT
# echo
# echo


# echo Multi-Genre Artists:
# find . | grep .ogg | cut -d "/" -f 2,3 | sort | uniq | cut -d "/" -f 2 | sort | uniq -d | while read artist
# do
#     echo  "$artist"

#     #find . | grep "$artist" | cut -d "/" -f 2 | sort | uniq | while read genre
#     #do
#     #    echo " $genre"
#     #done
#     #echo  "$(find . | grep "$artist" | cut -d "/" -f 2 | sort | uniq)"
#     artistGenre="$(find . | grep "$artist" | cut -d "/" -f 2 | sort | uniq)"
#     for genre in "$artistGenre"
#     do
#         echo " $genre"
#     done

# done

# echo 
# echo Multi-Disk Albums:
# find . | grep .ogg | grep disk | cut -d "/" -f 4 | sort | uniq | while read artist
# do
#     echo " $artist"
#     find . | grep "$artist" | grep .ogg | grep disk | cut -d "/" -f 4 | sort | uniq | while read album 
#     do 
#         echo "  $album"
#     done
# done