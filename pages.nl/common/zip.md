# zip

> Verpak en comprimeer (archiveer) bestanden in een Zip-archief.
> Bekijk ook: `unzip`.
> Meer informatie: <https://manned.org/zip>.

- Voeg bestanden/directories toe aan een specifiek archief ([r]ecursief):

`zip -r {{pad/naar/gecomprimeerd.zip}} {{pad/naar/bestand_of_directory1 pad/naar/bestand_of_directory2 ...}}`

- Verwijder bestanden/directories uit een specifiek archief ([d]elete):

`zip -d {{pad/naar/gecomprimeerd.zip}} {{pad/naar/bestand_of_directory1 pad/naar/bestand_of_directory2 ...}}`

- Archiveer bestanden/directories waarbij opgegeven bestanden worden uitgesloten:

`zip -r {{pad/naar/gecomprimeerd.zip}} {{pad/naar/bestand_of_directory1 pad/naar/bestand_of_directory2 ...}} -x {{pad/naar/uitgesloten_bestanden_of_directories}}`

- Archiveer bestanden/directories met een specifieke compressieniveau (`0` - het laagste, `9` - het hoogste):

`zip -r -{{0..9}} {{pad/naar/gecomprimeerd.zip}} {{pad/naar/bestand_of_directory1 pad/naar/bestand_of_directory2 ...}}`

- Maak een [e]ncrypted archief met een specifiek wachtwoord:

`zip -r -e {{pad/naar/gecomprimeerd.zip}} {{pad/naar/bestand_of_directory1 pad/naar/bestand_of_directory2 ...}}`

- Archiveer bestanden/directories in een multipart [s]plit Zip-archief (bijv. 3 GB delen):

`zip -r -s {{3g}} {{pad/naar/gecomprimeerd.zip}} {{pad/naar/bestand_of_directory1 pad/naar/bestand_of_directory2 ...}}`

- Print de inhoud van een specifiek archief:

`zip -sf {{pad/naar/gecomprimeerd.zip}}`
