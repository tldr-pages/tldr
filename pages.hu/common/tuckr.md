# tuckr

> Rust nyelven írt Dotfile menedzser. További információ: <https://github.com/RaphGL/Tuckr>.

- A dotfile állapotának ellenőrzése:

`tuckr status`

- Az összes dotfile hozzáadása a rendszerhez:

`tuckr add \*`

- Adja hozzá az összes dotfilet a megadott programok kivételével:

`tuckr add \* -e {{program1}},{{program2}}`

- Az összes dotfilet eltávolítása a rendszerből:

`tuckr rm \*`

- Egy program dotfile hozzáadása és beállítási szkriptjének futtatása:

`tuckr set {{program}}`
