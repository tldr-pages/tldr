# import

> Capturați o parte sau tot ecranul unui server X și salvați imaginea într-un fișier.
> Parte a bibliotecii ImageMagick.

- Capturează întregul ecran de server X în formatul de imagine PostScript:

`import -window root {{output.postscript}}`

- Capturează conținutul unui ecran de server X la distanță în formatul de imagine PNG:

`import -window root -display {{remote_host}}:{screen}.{display} {{output.png}}`

- Capturează o anumită fereastră, având în vedere ID-ul afișat de `xwininfo`, în format JPEG:

`import -window {{window_id}} {{output.jpg}}`
