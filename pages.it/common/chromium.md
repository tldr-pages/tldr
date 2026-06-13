# chromium

> Browser web open-source di Google.
> Maggiori informazioni: <https://www.chromium.org/developers/how-tos/run-chromium-with-flags/>.

- Apri un file:

`chromium {{percorso/del/file.html}}`

- Apri un URL:

`chromium {{esempio.com}}`

- Apri in modalità incognito:

`chromium --incognito {{esempio.com}}`

- Apri in una nuova finestra:

`chromium --new-window {{esempio.com}}`

- Apri in modalità app (senza barre degli strumenti, URL, bottoni, etc.):

`chromium --app='{{https://esempio.com}}'`

- Usa un server proxy:

`chromium --proxy-server="{{socks5://hostname:66}}" {{esempio.com}}`
