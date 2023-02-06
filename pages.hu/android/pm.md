# pm

> Információk megjelenítése az Android készüléken lévő alkalmazásokról. További információ: <https://developer.android.com/studio/command-line/adb#pm>.

- Az összes telepített alkalmazás listázása:

`pm list packages`

- Az összes telepített rendszeralkalmazás listázása:

`pm list packages -s`

- List all installed 3rd-Party apps:

`pm list packages -3`

- Bizonyos kulcsszavaknak megfelelő alkalmazások listázása:

`pm list packages {{keyword1 keyword2 ...}}`

- Egy adott alkalmazás APK-jának elérési útvonalának megjelenítése:

`pm path {{app}}`
