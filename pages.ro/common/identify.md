# identify

> Utilitar linie de comandă a proiectului Image Magick pentru a descrie formatul și caracteristicile unuia sau mai multor fișiere imagine.
> Mai multe informaţii: <https://imagemagick.org/script/identify.php>

- Colecta dimensiunile tuturor fișierelor jpeg în directorul curent:

`identify -format "%f,%w,%h\n" *.{{jpg}} > {{filelist.csv}}`
