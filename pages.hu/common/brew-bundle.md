# brew bundle

> Bundler for Homebrew, Homebrew Cask és a Mac App Store. További információ: <https://github.com/Homebrew/homebrew-bundle>.

- Csomagok telepítése egy Brewfile-ból az aktuális elérési útvonalra:

`brew bundle`

- Csomagok telepítése egy adott Brewfile-ból egy adott elérési útvonalra:

`brew bundle --file={{path/to/file}}`

- Brewfile létrehozása az összes telepített csomagból:

`brew bundle dump`

- A Brewfile-ban nem szereplő összes képlet eltávolítása:

`brew bundle cleanup --force`

- Ellenőrizze, hogy van-e valami telepítendő vagy frissítendő a Brewfile-ban:

`brew bundle check`

- A Brewfile-ban lévő összes bejegyzés listájának kiadása:

`brew bundle list --all`
