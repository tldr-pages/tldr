# aapt

> Instrumentul de ambalare a activelor Android.
> Compilați și împachetați resursele unei aplicații Android.
> Mai multe informaţii: <https://elinux.org/Android_aapt>

- Lista fișierelor conținute într-o arhivă APK:

`aapt list {{path/to/app.apk}}`

- Afișează metadatele unei aplicații (versiune, permisiuni etc.):

`aapt dump badging {{path/to/app.apk}}`

- Creați o nouă arhivă APK cu fișiere din directorul specificat:

`aapt package -F {{path/to/app.apk}} {{path/to/directory}}`
