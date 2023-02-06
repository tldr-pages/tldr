# git secret

> Bash eszköz, amely privát adatokat tárol egy Git repository-n belül. További információ: <https://github.com/sobolevn/git-secret>.

- A `git-secret` inicializálása egy helyi adattárban:

`git secret init`

- Hozzáférés biztosítása az aktuális Git felhasználó e-mailjéhez:

`git secret tell -m`

- Hozzáférés biztosítása e-mailben:

`git secret tell {{email}}`

- Hozzáférés visszavonása e-mailben:

`git secret killperson {{email}}`

- Titkokhoz hozzáféréssel rendelkező e-mailek listázása:

`git secret whoknows`

- Titkos fájl regisztrálása:

`git secret add {{path/to/file}}`

- Titkok titkosítása:

`git secret hide`

- Titkos fájlok visszafejtése:

`git secret reveal`
