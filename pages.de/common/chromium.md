# chromium

> Open-Source-Webbrowser von Google.
> Weitere Informationen: <https://www.chromium.org/developers/how-tos/run-chromium-with-flags/>.

- Öffne eine html-Datei:

`chromium {{pfad/zu/datei.html}}`

- Öffne eine bestimmte URL:

`chromium {{beispiel.com}}`

- Öffne eine URL im Inkognito-Modus:

`chromium --incognito {{beispiel.com}}`

- Öffne eine URL in einem neuen Fenster:

`chromium --new-window {{beispiel.com}}`

- Öffne eine URL im Anwendungsmodus (ohne Symbolleisten, Suchleiste, Schaltflächen usw.):

`chromium --app='{{https://beispiel.com}}'`

- Öffne eine URL und verwende einen Proxy-Server:

`chromium --proxy-server="{{socks5://hostname:66}}" {{beispiel.com}}`
