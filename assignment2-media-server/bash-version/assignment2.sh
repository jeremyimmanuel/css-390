#! /bin/bash

echo "<html>" > index.html
echo "<meta http-equiv=\"content-type\" content=\"text/html; charset=utf-8\" />" >> index.html
echo "<body><table border=\"1\">" >> index.html
( echo "<tr>" ; echo "<th>Artist</th>" ; echo "<th>Album</th>" ; echo "<th>Tracks</th>" ; echo "</tr>") >> index.html

find . | grep .ogg | sort | cut -d "/" -f4 | sort | uniq |
while read artist
do
    count=0
    find . | grep .ogg | grep "$artist\/"  | cut -d "/" -f5 | sort | uniq | 
    while read album
    do
        echo "<tr>" >> index.html
        if [ $count == 0 ]
        then
            rs="$(find . | grep .ogg | grep "$artist\/"  | cut -d "/" -f5 | sort | uniq | wc -l)"
            echo "<td rowspan=\"$rs\">$artist</td>" >> index.html
        fi
        
        echo "<td>$album</td>" >> index.html
        ( echo "<td>" ; echo "<table border=\"0\">") >> index.html
        
        find . | grep .ogg | grep "$artist\/" | grep  "$album\/" | sort |
        while read song
        do 
            songTitle="$(basename -- $song | sed -e 's/\<'"$album"'>//')"
            echo "<tr><td><a href=\""$song"\"> "$songTitle" </a></td</tr>" >> index.html
        done
        ( echo "</table>" ; echo "</td>") >> index.html
        echo "</tr>" >> index.html
        count=($count+1)
    done
done
echo "</table>" >> index.html
echo "</body>" >> index.html
