import json
import os

def jsonreader(ajsonfile):
    f = open(ajsonfile, encoding="ANSI")
    data = json.load(f)
    return data

def listofurltowebsite(listofurls):
    imgdir = os.getcwd() + "\\"
    f = open(imgdir + 'cube.html', 'w')
    f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="stylesheet" href="main.css">
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Generated Cube</title>
</head>
<body><div>""")
    # for urlname in urldicte.keys():
    #     f.write('<img src="'+urlname+'.png">')
    i = 0
    thestr = ""
    for url in listofurls:
        f.write('<img src="' + url + '">\n')
    f.write("""</div></body>
</html>""")
    f.close()
    os.system(imgdir + 'cube.html')