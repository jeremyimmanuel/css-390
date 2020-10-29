import html, os

genre = os.listdir(os.getcwd() + '/Music')
artist_dict = {}

for g in genre:
    artist_dict.update(dict.fromkeys(os.listdir(os.path.join(os.getcwd(), 'Music', g))))

for k in artist_dict:
    artist_dict[k] = []

for g in genre:
    for dirPath, folders, filenames in os.walk(os.path.join(os.getcwd(), 'Music', g)):
        if os.path.split(dirPath)[-1] in artist_dict.keys() and dirPath.split('/')[-1] != dirPath.split('/')[-2]:
                albums = os.listdir(dirPath)
                for alb in albums:
                    alb_t = '\n\t<td>%s</td>' % alb
                    song_t = '\t\t<td>\n\t\t<table border="0">\n'
                    if os.listdir(os.path.join(dirPath, alb))[0][-4:] == '.ogg':
                        songs = sorted(os.listdir(os.path.join(dirPath, alb)))
                        #song_t += '\n'
                        for s in songs:
                            song_t += '\t\t\t<tr><td><a href="%s">%s</a></td></tr>\n' % (os.path.join(dirPath, alb, s), s[:-4])
                    else: 
                        for diskPath, diskDir, songs in os.walk(os.path.join(dirPath, alb)):
                            songs = sorted(songs)
                            if len(songs) > 0:
                                for s in songs:
                                    song_t += '\t\t\t<tr><td><a href="%s">%s</a></td></tr>\n' % (os.path.join(diskPath, s), s[:-4])
                    song_t += '\t\t</table>\n\t</td>\n'

                    alb_t += '\n' + song_t
                    
                    ak = os.path.split(dirPath)[-1]
                    artist_dict[ak].append(alb_t)

table = '<html>\n<meta http-equiv="content-type" content="text/html; charset=utf-8"/>\n<body>\n<table border = "1">\n<tr>\n\t<th>Artist</th>\n\t<th>Album</th>\n\t<th>Tracks</th>\n</tr>\n'

for artist in sorted(artist_dict):
    a = ''
    for album in sorted(artist_dict[artist]):
        a += '<tr>%s</tr>\n' % album
    
    art = '\n<td rowspan="%d">%s</td>\n' % (len(artist_dict[artist]), artist)
    #print(art)
    a = a[:4] + art + a[4:]
    table += a

table += '\n</table>\n</body>'
# open("index.html", 'w', encoding='utf-8').write(html.escape(table))
f = open('index.html', 'w')
f.write(table)


