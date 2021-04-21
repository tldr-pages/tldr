# pm

> Zeige Informationen über Apps auf einem Android Gerät.
> Mehr Informationen: <https://developer.android.com/studio/command-line/adb#pm>.

- Gib eine Liste aller installierten Apps aus:

`pm list packages`

- Gib eine Liste aller installierten System-Apps aus:

`pm list packages -s`

- Gib eine liste aller installierten 3rd-Party apps aus:

`pm list packages -3`

- Gib eine Liste aller Apps, die auf ein bestimmtes Schlüsselwort zutreffen aus:

`pm list packages {{Schlüsselwort}}`

- Gib den Pfad der APK einer bestimmten App aus:

`pm path {{app}}`
