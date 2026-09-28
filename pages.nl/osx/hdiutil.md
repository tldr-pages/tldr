# hdiutil

> Hulpprogramma voor het maken en beheren van disk images.
> Meer informatie: <https://keith.github.io/xcode-man-pages/hdiutil.1.html>.

- Koppel een image aan:

`hdiutil attach {{pad/naar/image_bestand}}`

- Ontkoppel een image:

`hdiutil detach /Volumes/{{volume_bestand}}`

- Toon aangekoppelde images:

`hdiutil info`

- Maak een ISO-image van de inhoud van een map:

`hdiutil makehybrid -o {{pad/naar/uitvoerbestand}} {{pad/naar/map}}`
