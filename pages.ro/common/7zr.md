# 7zr

> Arhivator de fișiere cu un raport de compresie ridicat.
> Similar cu `7z`, cu excepția faptului că acceptă numai fișiere `.7z`.
> Mai multe informaţii: <https://www.7-zip.org>

- [a] rchive un fișier sau un director:

`7zr a {{path/to/archive.7z}} {{path/to/file_or_directory}}`

- Criptați o arhivă existentă (inclusiv nume de fișiere):

`7zr a {{path/to/encrypted.7z}} -p{{password}} -mhe=on {{path/to/archive.7z}}`

- E [x] tractează o arhivă păstrând structura originală a directorului:

`7zr x {{path/to/archive.7z}}`

- E [x] tract o arhivă la un anumit director:

`7zr x {{path/to/archive.7z}} -o{{path/to/output}}`

- E [x] tractează o arhivă la stdout:

`7zr x {{path/to/archive.7z}} -so`

- [l] ist conținutul unei arhive:

`7zr l {{path/to/archive.7z}}`

- Lista tipurilor de arhive disponibile:

`7zr i`
