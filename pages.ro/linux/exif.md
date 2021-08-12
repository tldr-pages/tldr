# exif

> Afișați și modificați informațiile EXIF din fișierele JPEG.
> Mai multe informaţii: <https://github.com/libexif/exif/>

- Afișează toate informațiile EXIF recunoscute într-o imagine:

`exif {{path/to/image.jpg}}`

- Afișați un tabel care conține etichete EXIF cunoscute și dacă fiecare dintre ele există într-o imagine:

`exif --list-tags --no-fixup {{image.jpg}}`

- Extrageţi miniatura imaginii în fişierul `thumbnail.jpg`:

`exif --extract-thumbnail --output={{thumbnail.jpg}} {{image.jpg}}`

- Afișați conținutul brut al etichetei „Model” în imaginea dată:

`exif --ifd={{0}} --tag={{Model}} --machine-readable {{image.jpg}}`

- Modificați valoarea etichetei „Artist” în John Smith și salvați în `new.jpg`:

`exif --output={{new.jpg}} --ifd={{0}} --tag="{{Artist}}" --set-value="{{John Smith}}" --no-fixup {{image.jpg}}`
