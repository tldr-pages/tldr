# bower

> Front-end webfejlesztésre optimalizált csomagkezelő. A csomag lehet egy GitHub felhasználó/repo rövidítés, egy Git végpont, egy URL vagy egy regisztrált csomag. További információ: <https://bower.io/>.

- Telepíti egy projekt függőségeit, amelyek a bower.json-ban vannak felsorolva:

`bower install`

- Telepítsen egy vagy több csomagot a bower_components könyvtárba:

`bower install {{package}} {{package}}`

- A csomagok helyi eltávolítása a bower_components könyvtárból:

`bower uninstall {{package}} {{package}}`

- A helyi csomagok és a lehetséges frissítések listázása:

`bower list`

- Súgóinformációk megjelenítése egy bower-paranccsal kapcsolatban:

`bower help {{command}}`

- `bower.json` fájl létrehozása a csomaghoz:

`bower init`

- Egy adott függőségi verzió telepítése, és hozzáadása a `bower.json`:

`bower install {{local_name}}={{package}}#{{version}} --save`
