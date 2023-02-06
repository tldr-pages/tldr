# export

> Parancs az aktuális környezetben lévő héjváltozók megjelölésére, hogy azokat az újonnan elágazó gyermekfolyamatokkal együtt exportálják. További információ: <https://www.gnu.org/software/bash/manual/bash.html#index-export>.

- Új környezeti változó beállítása:

`export {{VARIABLE}}={{value}}`

- Környezeti változó eltávolítása:

`export -n {{VARIABLE}}`

- Egy héjfüggvényt jelölni exportálásra:

`export -f {{FUNCTION_NAME}}`

- Hozzáadni valamit a PATH változóhoz:

`export PATH=$PATH:{{path/to/append}}`
