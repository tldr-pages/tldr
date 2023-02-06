# zoxide

> Nyomon követi a leggyakrabban használt könyvtárakat. Egy rangsoroló algoritmust használ a legjobb találathoz való navigáláshoz. További információ: <https://github.com/ajeetdsouza/zoxide>.

- Menjen a legmagasabb rangsorú könyvtárba, amelynek nevében szerepel a "foo":

`zoxide query {{foo}}`

- Menjen a legmagasabb rangsorolt könyvtárba, amely tartalmazza a "foo", majd a "bar" szót:

`zoxide query {{foo}} {{bar}}`

- Interaktív könyvtárkeresés indítása ( `fzf`):

`zoxide query --interactive`

- Könyvtár hozzáadása vagy rangjának növelése:

`zoxide add {{path/to/directory}}`

- Könyvtárak interaktív eltávolítása a `zoxide` adatbázisából:

`zoxide remove {{path/to/directory}} --interactive`

- Héjkonfiguráció létrehozása a parancs aliasokhoz (`z`, `za`, `zi`, `zq`, `zr`):

`zoxide init {{bash|fish|zsh}}`
