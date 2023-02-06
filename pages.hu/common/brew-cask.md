# brew --cask

> CLI-munkafolyamat a bináris formában terjesztett macOS-alkalmazások adminisztrációjához. Ezt a parancsot korábban `brew cask` néven használták, deprecated (elavult) a `brew --cask` flag javára. További információ: <https://github.com/Homebrew/homebrew-cask>.

- Képletek és hordók keresése:

`brew search {{text}}`

- Telepítsen egy hordót:

`brew install --cask {{cask_name}}`

- Az összes telepített hordó listázása:

`brew list --cask`

- Azon telepített hordók listázása, amelyeknek újabb verziója elérhető:

`brew outdated --cask`

- Egy telepített hordó frissítése (ha nincs megadva a hordó neve, akkor az összes telepített hordó frissül):

`brew upgrade --cask {{cask_name}}`

- Egy hordó eltávolítása:

`brew uninstall --cask {{cask_name}}`

- A hordó eltávolítása és a kapcsolódó beállítások és fájlok eltávolítása:

`brew zap --cask {{cask_name}}`

- Információk megjelenítése egy adott hordóról:

`brew info --cask {{cask_name}}`
