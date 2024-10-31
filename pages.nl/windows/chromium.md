# chromium

> Open-source webbrowser die voornamelijk ontwikkeld en onderhouden wordt door Google.
> Opmerking: Mogelijk moet je het `chromium` commando vervangen met jouw gewenste webbrowser, zoals `brave`, `google-chrome`, `microsoft-edge`/`msedge`, `opera`, of `vivaldi`.
> Meer informatie: <https://www.chromium.org/developers/how-tos/run-chromium-with-flags/>.

- Open een specifieke URL of bestand:
  
`chromium {{https://voorbeeld.com|path/naar/bestand.html}}`

- Open in incognito modus (gebruik `--inprivate` voor Microsoft Edge):
  
`{{chromium --incognito|msedge --inprivate}} {{voorbeeld.com}}`

- Open in een nieuw venster:
  
`chromium --new-window {{voorbeeld.com}}`

- Open in applicatie modus (zonder werkbalken, URL balk, knoppen, etc.):
  
`chromium --app={{https://voorbeeld.com}}`

- Gebruik een proxy server:
  
`chromium --proxy-server="{{socks5://hostname:66}}" {{voorbeeld.com}}`

- Open met een aangepaste profiel map:
  
`chromium --user-data-dir={{path/to/directory}}`

- Open zonder CORS validatie (handig om een API te testen):
  
`chromium --user-data-dir={{path/to/directory}} --disable-web-security`

- Open met een DevTools venster voor elk geopend tabblad:
  
`chromium --auto-open-devtools-for-tabs`
