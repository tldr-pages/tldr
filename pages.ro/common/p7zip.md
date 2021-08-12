# p7zip

> Învelișul arhivatorului de fișiere 7-Zip cu raport de compresie ridicat.
> Execută intern fie comanda 7za sau 7zr.
> Mai multe informaţii: <http://p7zip.sourceforge.net>

- Arhivați un fișier, înlocuindu-l cu o versiune comprimată 7zip:

`p7zip {{path/to/file}}`

- Arhivează un fișier care păstrează fișierul de intrare:

`p7zip -k {{path/to/file}}`

- Decomprima un fișier, înlocuindu-l cu versiunea originală necomprimată:

`p7zip -d {{compressed.ext}}.7z`

- Decomprima un fișier care păstrează fișierul de intrare:

`p7zip -d -k {{compressed.ext}}.7z`

- Treci peste unele verificări și forța de compresie sau decompresie:

`p7zip -f {{path/to/file}}`
