# androguard

> Reverse engineering tool voor Android-applicaties, geschreven in Python.
> Meer informatie: <https://github.com/androguard/androguard>.

- Toon het manifest van de Android-app:

`androguard axml {{pad/naar/app}}.apk`

- Toon de metadata van de app (versie en app ID):

`androguard apkid {{pad/naar/app}}.apk`

- Decompileer Java code van een applicatie:

`androguard decompile {{pad/naar/app}}.apk --output {{pad/naar/map}}`
