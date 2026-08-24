# chromium

> Browser web open-source sviluppato e mantenuto principalmente da Google.
> Nota: potrebbe essere necessario sostituire il comando `chromium` con il browser desiderato, come `brave`, `google-chrome`, `opera` o `vivaldi`.
> Maggiori informazioni: <https://www.chromium.org/developers/how-tos/run-chromium-with-flags/>.

- Apri un URL o un file specifico:

`chromium {{https://example.com|percorso/del/file.html}}`

- Apri in modalità incognito:

`chromium --incognito {{esempio.com}}`

- Apri in una nuova finestra:

`chromium --new-window {{esempio.com}}`

- Apri in modalità applicazione (senza barre degli strumenti, barra URL, pulsanti, ecc.):

`chromium --app={{https://esempio.com}}`

- Usa un server proxy:

`chromium --proxy-server="{{socks5://hostname:66}}" {{esempio.com}}`

- Apri con una directory di profilo personalizzata:

`chromium --user-data-dir={{percorso/della/directory}}`

- Apri senza validazione CORS (utile per testare un'API):

`chromium --user-data-dir={{percorso/della/directory}} --disable-web-security`

- Apri con una finestra DevTools per ogni scheda aperta:

`chromium --auto-open-devtools-for-tabs`
