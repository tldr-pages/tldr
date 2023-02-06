# pageres

> Képernyőképek készítése weboldalakról különböző felbontásokban. További információ: <https://github.com/sindresorhus/pageres-cli>.

- Készítsen több képernyőképet több URL-címről különböző felbontásban:

`pageres {{https://example.com/}} {{https://example2.com/}} {{1366x768}} {{1600x900}}`

- Adjon meg konkrét beállításokat egy URL-hez, felülírva a globális beállításokat:

`pageres [{{https://example.com/}} {{1366x768}} --no-crop] [{{https://example2.com/}} {{1024x768}}] --crop`

- Egyéni fájlnévsablon megadása:

`pageres {{https://example.com/}} {{1024x768}} --filename={{'<%= date %> - <%= url %>'}}`

- Egy adott elem rögzítése egy oldalon:

`pageres {{https://example.com/}} {{1366x768}} --selector='{{.page-header}}'`

- Egy adott elem elrejtése:

`pageres {{https://example.com/}} {{1366x768}} --hide='{{.page-header}}'`

- Képernyőkép készítése egy helyi fájlról:

`pageres {{local_file_path.html}} {{1366x768}}`
