# chromium

> Open-source webbrowser die voornamelijk ontwikkeld en onderhouden wordt door Google.
> Let op: mogelijk moet je het `chromium` commando vervangen met jouw gewenste webbrowser, zoals `brave`, `google-chrome`, `microsoft-edge`/`msedge`, `opera` of `vivaldi`.
> Meer informatie: <https://www.chromium.org/developers/how-tos/run-chromium-with-flags/>.

- Open een specifieke URL of bestand:

`chromium {{https://example.com|path\naar\bestand.html}}`

- Open in incognito modus (gebruik `--inprivate` voor Microsoft Edge):

`{{chromium --incognito|msedge --inprivate}} {{example.com}}`

- Open in een nieuw venster:

`chromium --new-window {{example.com}}`

- Open in applicatie modus (zonder werkbalken, URL balk, knoppen, etc.):

`chromium --app {{https://example.com}}`

- Gebruik een proxy server:

`chromium --proxy-server "{{socks5://hostname:66}}" {{example.com}}`

- Open met een aangepaste profiel map:

`chromium --user-data-dir {{pad\naar\map}}`

- Open zonder CORS validatie (handig om een API te testen):

`chromium --user-data-dir {{pad\naar\map}} --disable-web-security`

- Open met een DevTools venster voor elk geopend tabblad:

`chromium --auto-open-devtools-for-tabs`
