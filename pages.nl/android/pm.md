# pm

> Toon informatie over apps op een Android-apparaat.
> Meer informatie: <https://developer.android.com/studio/command-line/adb#pm>.

- Maak een lijst van alle geïnstalleerde apps:

`pm list packages`

- Maak een lijst van alle geïnstalleerde systeem-apps:

`pm list packages -s`

- Maak een lijst van alle geïnstalleerde apps van 3e partijen:

`pm list packages -3`

- Maak een lijst met apps die overeenkomen met specifieke trefwoorden:

`pm list packages {{keyword1 keyword2 ...}}`

- Toon een pad van de APK van een specifieke app:

`pm path {{app}}`
