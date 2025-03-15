# zip

> Verpak en comprimeer (archiveer) bestanden in een Zip-archief.
> Bekijk ook: `unzip`.
> Meer informatie: <https://manned.org/zip>.

- Voeg bestanden/directories toe aan een specifiek archief:

`zip {{[-r|--recurse-paths}} {{pad/naar/gecomprimeerd.zip}} {{pad/naar/bestand_of_directory1 pad/naar/bestand_of_directory2 ...}}`

- Verwijder bestanden/directories uit een specifiek archief:

`zip {{[-d|--delete]}} {{pad/naar/gecomprimeerd.zip}} {{pad/naar/bestand_of_directory1 pad/naar/bestand_of_directory2 ...}}`

- Archiveer bestanden/directories waarbij opgegeven bestanden worden uitgesloten:

`zip {{pad/naar/gecomprimeerd.zip}} {{pad/naar/bestand_of_directory1 pad/naar/bestand_of_directory2 ...}} {{-x|--exclude}} {{pad/naar/uitgesloten_bestanden_of_directories}}`

- Archiveer bestanden/directories met een specifieke compressieniveau (`0` - het laagste, `9` - het hoogste):

`zip {{[-r|--recurse-paths}} -{{0..9}} {{pad/naar/gecomprimeerd.zip}} {{pad/naar/bestand_of_directory1 pad/naar/bestand_of_directory2 ...}}`

- Maak een versleuteld archief met een specifiek wachtwoord:

`zip {{[-r|--recurse-paths}} {{[-e|--encrypt]}} {{pad/naar/gecomprimeerd.zip}} {{pad/naar/bestand_of_directory1 pad/naar/bestand_of_directory2 ...}}`

- Archiveer bestanden/directories in een multipart [s]plit Zip-archief (bijv. 3 GB delen):

`zip {{[-r|--recurse-paths}} {{[-s|--split-size]}} {{3g}} {{pad/naar/gecomprimeerd.zip}} {{pad/naar/bestand_of_directory1 pad/naar/bestand_of_directory2 ...}}`

- Toon de inhoud van een specifiek archief:

`zip {{[-sf|--split-size --freshen]}} {{pad/naar/gecomprimeerd.zip}}`
