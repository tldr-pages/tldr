# rvm

> Egy eszköz több ruby környezet egyszerű telepítéséhez, kezeléséhez és munkájához. További információ: <https://rvm.io>.

- A Ruby egy vagy több, szóközzel elválasztott verziójának telepítése:

`rvm install {{version(s)}}`

- A telepített verziók listájának megjelenítése:

`rvm list`

- A Ruby egy adott verziójának használata:

`rvm use {{version}}`

- Ruby alapértelmezett verziójának beállítása:

`rvm --default use {{version}}`

- A Ruby egy verziójának frissítése egy új verzióra:

`rvm upgrade {{current_version}} {{new_version}}`

- A Ruby egy verziójának eltávolítása és forrásainak megtartása:

`rvm uninstall {{version}}`

- A Ruby egy verziójának és forrásainak eltávolítása:

`rvm remove {{version}}`

- Megjelenítheti az operációs rendszer specifikus függőségeit:

`rvm requirements`
