# androguard

> Instrument de inginerie inversă pentru aplicații Android. Scrisă în Python.
> Mai multe informaţii: <https://github.com/androguard/androguard>

- Afișează manifestul aplicației Android:

`androguard axml {{path/to/app.apk}}`

- Afişarea metadatelor aplicaţiei (versiunea şi ID-ul aplicaţiei):

`androguard apkid {{path/to/app.apk}}`

- Decompila codul Java dintr-o aplicație:

`androguard decompile {{path/to/app.apk}} --output {{path/to/directory}}`
