# aapt

> Android Asset Packaging-tool.
> Compileer en verpak de bronnen van een Android-app.
> Meer Informatie: <https://elinux.org/Android_aapt>.

- Maak een lijst van bestanden in een APK-archief:

`aapt list {{pad/naar/app.apk}}`

- Geef de metadata van een app weer (versie, machtigingen, enz.):

`aapt dump badging {{pad/naar/app.apk}}`

- Maak een nieuw APK-archief met bestanden uit de opgegeven map:

`aapt package -F {{pad/naar/app.apk}} {{pad/naar/directory}}`
