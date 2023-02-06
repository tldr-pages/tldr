# pactree

> Csomagfüggőségi fa megjelenítője a pacman számára. További információ: <https://man.archlinux.org/man/pactree.8>.

- Egy adott csomag függőségi fájának kinyomtatása:

`pactree {{package}}`

- Kiírja, hogy mely csomagok függenek egy adott csomagtól:

`pactree --reverse {{package}}`

- A függőségek soronkénti kiírása, a duplikációk kihagyásával:

`pactree --unique {{package}}`

- Egy adott csomag opcionális függőségeinek felvétele és a kimenet színezése:

`pactree --optional --color {{package}}`

- Súgó megjelenítése:

`pactree`
