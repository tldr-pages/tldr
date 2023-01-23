# codesign

> Kódaláírások létrehozása és kezelése a macOS számára. További információ: <https://www.unix.com/man-page/osx/1/codesign/>.

- Alkalmazás aláírása tanúsítvánnyal:

`codesign --sign "{{My Company Name}}" {{path/to/App.app}}`

- Egy alkalmazás tanúsítványának ellenőrzése:

`codesign --verify {{path/to/App.app}}`
