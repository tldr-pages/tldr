# pyenv

> Könnyen válthat több Python-verzió között. További információ: <https://github.com/pyenv/pyenv>.

- Az összes elérhető parancs listája:

`pyenv commands`

- A `${PYENV_ROOT}/versions` könyvtár alatt található összes Python-verzió listázása:

`pyenv versions`

- Listázza az összes Python verziót, amely telepíthető az upstreamről:

`pyenv install --list`

- Telepítsen egy Python verziót a `${PYENV_ROOT}/versions` könyvtár alá:

`pyenv install {{2.7.10}}`

- A `${PYENV_ROOT}/versions` könyvtár alatti Python-verzió eltávolítása:

`pyenv uninstall {{2.7.10}}`

- Az aktuális gépen globálisan használandó Python-verzió beállítása:

`pyenv global {{2.7.10}}`

- Az aktuális könyvtárban és az alatta lévő összes könyvtárban használandó Python-verzió beállítása:

`pyenv local {{2.7.10}}`
