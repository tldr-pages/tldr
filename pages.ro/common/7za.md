# 7za

> Arhivator de fișiere cu un raport de compresie ridicat.
> Similar cu `7z`, cu excepția faptului că acceptă mai puține tipuri de fișiere, dar este cross-platform.
> Mai multe informaţii: <https://www.7-zip.org>

- [a] rchive un fișier sau un director:

`7za a {{path/to/archive.7z}} {{path/to/file_or_directory}}`

- Criptați o arhivă existentă (inclusiv nume de fișiere):

`7za a {{path/to/encrypted.7z}} -p{{password}} -mhe=on {{path/to/archive.7z}}`

- E [x] tractează o arhivă păstrând structura originală a directorului:

`7za x {{path/to/archive.7z}}`

- E [x] tract o arhivă la un anumit director:

`7za x {{path/to/archive.7z}} -o{{path/to/output}}`

- E [x] tractează o arhivă la stdout:

`7za x {{path/to/archive.7z}} -so`

- [a] rchive folosind un anumit tip de arhivă:

`7z a -t{{7z|zip|gzip|bzip2|lzip}} {{path/to/archive.7z}} {{path/to/file_or_directory}}`

- [l] ist conținutul unei arhive:

`7za l {{path/to/archive.7z}}`

- Lista tipurilor de arhive disponibile:

`7za i`
