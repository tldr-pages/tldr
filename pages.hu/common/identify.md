# identify

> Az Image Magick projekt parancssori segédprogramja egy vagy több képfájl formátumának és jellemzőinek leírására. További információ: <https://imagemagick.org/script/identify.php>.

- Egy kép formátumának és alapvető jellemzőinek leírása:

`identify {{path/to/image}}`

- Egy kép formátumának és szóbeli jellemzőinek leírása:

`identify -verbose {{path/to/image}}`

- Az aktuális könyvtárban található összes JPEG-fájl méretének összegyűjtése:

`identify -format "%f,%w,%h\n" *.{{jpg}} > {{path/to/filelist.csv}}`
