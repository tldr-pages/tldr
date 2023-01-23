# rbenv

> Egy eszköz a Ruby verziók egyszerű telepítéséhez és az alkalmazáskörnyezetek kezeléséhez. További információ: <https://github.com/rbenv/rbenv>.

- Ruby verzió telepítése:

`rbenv install {{version}}`

- Az egyes Ruby-verziók legújabb stabil verzióinak listájának megjelenítése:

`rbenv install --list`

- A telepített Ruby-verziók listájának megjelenítése:

`rbenv versions`

- Egy adott Ruby-verzió használata az egész rendszerben:

`rbenv global {{version}}`

- Egy adott Ruby-verzió használata egy alkalmazás/projektkönyvtárhoz:

`rbenv local {{version}}`

- Az aktuálisan kiválasztott Ruby-verzió megjelenítése:

`rbenv version`

- Egy Ruby-verzió eltávolítása:

`rbenv uninstall {{version}}`

- A megadott futtatható fájlt tartalmazó összes Ruby-verzió megjelenítése:

`rbenv whence {{executable}}`
