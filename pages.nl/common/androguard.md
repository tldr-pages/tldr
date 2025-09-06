# androguard

> Reverse engineering tool voor Android applicaties, geschreven in Python.
> Meer informatie: <https://github.com/androguard/androguard>.

- Toon Android app manifest:

`androguard axml {{pad/naar/app.apk}}`

- Toon app metadata (versie en app ID):

`androguard apkid {{pad/naar/app.apk}}`

- Decompileer Java code van een applicatie:

`androguard decompile {{pad/naar/app.apk}} --output {{pad/naar/map}}`
