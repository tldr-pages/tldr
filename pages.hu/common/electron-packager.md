# electron-packager

> Az Electron alkalmazások Windows, Linux és macOS futtatható fájljainak elkészítéséhez használt eszköz. Érvényes package.json fájl szükséges az alkalmazás könyvtárában. További információ: <https://github.com/electron/electron-packager>.

- Csomagolja az alkalmazást az aktuális architektúrához és platformhoz:

`electron-packager "{{path/to/app}}" "{{app_name}}"`

- Alkalmazás csomagolása minden architektúrára és platformra:

`electron-packager "{{path/to/app}}" "{{app_name}}" --all`

- Alkalmazás csomagolása 64 bites Linuxhoz:

`electron-packager "{{path/to/app}}" "{{app_name}}" --platform="{{linux}}" --arch="{{x64}}"`

- Alkalmazás csomagolása ARM macOS-re:

`electron-packager "{{path/to/app}}" "{{app_name}}" --platform="{{darwin}}" --arch="{{arm64}}"`
