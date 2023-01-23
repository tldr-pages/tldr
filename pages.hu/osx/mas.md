# mas

> Parancssori felület a Mac App Store-hoz. További információ: <https://github.com/mas-cli/mas>.

- Jelentkezzen be először a Mac App Store-ba:

`mas signin "{{user@example.com}}"`

- Megjeleníti az összes telepített alkalmazást és azok termékazonosítóját:

`mas list`

- Alkalmazás keresése, a találatok mellett az ár megjelenítésével:

`mas search "{{application}}" --price`

- Alkalmazás telepítése vagy frissítése:

`mas install {{product_identifier}}`

- Az összes függőben lévő frissítés telepítése:

`mas upgrade`
