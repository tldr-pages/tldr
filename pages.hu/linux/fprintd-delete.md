# fprintd-delete

> Ujjlenyomatok eltávolítása az adatbázisból. További információ: <https://manned.org/fprintd-delete>.

- Egy adott felhasználó összes ujjlenyomatának eltávolítása:

`fprintd-delete {{username}}`

- Bizonyos ujjlenyomatok eltávolítása egy adott felhasználóhoz:

`fprintd-delete {{username}} --finger {{left-thumb|left-index-finger|left-middle-finger|left-ring-finger|left-little-finger|right-thumb|right-index-finger|right-middle-finger|right-ring-finger|right-little-finger}}`

- Súgó megjelenítése:

`fprintd-delete`
