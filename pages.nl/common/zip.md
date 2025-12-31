# zip

> Verpak en comprimeer (archiveer) bestanden in een Zip-archief.
> Zie ook: `unzip`.
> Meer informatie: <https://manned.org/zip>.

- Voeg bestanden/mappen toe aan een specifiek archief:

`zip {{[-r|--recurse-paths]}} {{pad/naar/gecomprimeerd.zip}} {{pad/naar/bestand_of_map1 pad/naar/bestand_of_map2 ...}}`

- Verwijder bestanden/mappen uit een specifiek archief:

`zip {{[-d|--delete]}} {{pad/naar/gecomprimeerd.zip}} {{pad/naar/bestand_of_map1 pad/naar/bestand_of_map2 ...}}`

- Archiveer bestanden/mappen waarbij opgegeven bestanden worden uitgesloten:

`zip {{[-r|--recurse-paths]}} {{pad/naar/gecomprimeerd.zip}} {{pad/naar/bestand_of_map1 pad/naar/bestand_of_map2 ...}} {{[-x|--exclude]}} {{pad/naar/uitgesloten_bestanden_of_mappen}}`

- Archiveer bestanden/mappen met een specifieke compressieniveau (`0` - het laagste, `9` - het hoogste):

`zip {{[-r|--recurse-paths]}} -{{0..9}} {{pad/naar/gecomprimeerd.zip}} {{pad/naar/bestand_of_map1 pad/naar/bestand_of_map2 ...}}`

- Maak een encrypted archief met een specifiek wachtwoord:

`zip {{[-re|--recurse-paths --encrypt]}} {{pad/naar/gecomprimeerd.zip}} {{pad/naar/bestand_of_map1 pad/naar/bestand_of_map2 ...}}`

- Archiveer bestanden/mappen in een multipart split Zip-archief (bijv. 3 GB delen):

`zip {{[-rs|--recurse-paths --split-size]}} {{3g}} {{pad/naar/gecomprimeerd.zip}} {{pad/naar/bestand_of_map1 pad/naar/bestand_of_map2 ...}}`

- Print de inhoud van een specifiek archief:

`zip {{[-sf|--split-size --freshen]}} {{pad/naar/gecomprimeerd.zip}}`
