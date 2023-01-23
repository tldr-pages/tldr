# finger

> Egy megadott rendszer egy vagy több felhasználójáról ad vissza információt. A távoli rendszeren a Finger szolgáltatásnak kell futnia. További információ: <https://learn.microsoft.com/windows-server/administration/windows-commands/finger>.

- Információk megjelenítése egy adott felhasználóról:

`finger {{user}}@{{host}}`

- A megadott állomáson lévő összes felhasználóról szóló információk megjelenítése:

`finger @{{host}}`

- Hosszabb formátumú információk megjelenítése:

`finger {{user}}@{{host}} -l`

- Súgóinformációk megjelenítése:

`finger /?`
