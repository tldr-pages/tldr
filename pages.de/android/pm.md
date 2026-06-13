# pm

> Zeige Informationen über Apps auf einem Android Gerät.
> Weitere Informationen: <https://developer.android.com/tools/adb#pm>.

- Gib eine Liste aller installierten Apps aus:

`pm list packages`

- Gib eine Liste aller installierten System-Apps aus:

`pm list packages -s`

- Gib eine Liste aller installierten Apps von Drittanbietern aus:

`pm list packages -3`

- Gib eine Liste aller Apps, auf die ein bestimmtes Schlüsselwort zutrifft, aus:

`pm list packages {{Schlüsselwort}}`

- Gib den Pfad der APK einer bestimmten App aus:

`pm path {{app}}`
