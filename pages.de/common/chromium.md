# chromium

> Open-Source-Webbrowser von Google.
> Weitere Informationen: <https://www.chromium.org/developers/how-tos/run-chromium-with-flags/>.

- Öffne eine bestimmte Datei oder URL:

`chromium {{https://beispiel.com|pfad/zu/datei.html}}`

- Öffne eine URL im Inkognito-Modus:

`chromium --incognito {{beispiel.com}}`

- Öffne eine URL in einem neuen Fenster:

`chromium --new-window {{beispiel.com}}`

- Öffne eine URL im Anwendungsmodus (ohne Symbolleisten, Suchleiste, Schaltflächen usw.):

`chromium --app={{https://beispiel.com}}`

- Öffne eine URL und verwende einen Proxy-Server:

`chromium --proxy-server="{{socks5://hostname:66}}" {{beispiel.com}}`

- Öffne Chromium mit einem eigenen Profil-Verzeichnis:

`chromium --user-data-dir={{pfad/zu/verzeichnis}}`

- Öffne Chromium ohne CORS-Verifizierung (nützlich, um eine API zu testen):

`chromium --user-data-dir={{pfad/zu/verzeichnis}} --disable-web-security`

- Öffne Chromium mit einem `DevTools`-Fenster für jeden geöffneten Tab:

`chromium --auto-open-devtools-for-tabs`
