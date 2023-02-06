# colorpicker

> Egy minimalista X11 színválasztó. Bármilyen egérmozdulat, kivéve a bal kattintást, kilép a programból. További információ: <https://github.com/ym1234/colorpicker>.

- Elindítja a színválasztót, és minden egyes kattintott pixel hexadecimális és RGB értékét kiírja a `stdout` címre:

`colorpicker`

- Csak egy kattintott pixel színét nyomtassa ki, majd lépjen ki:

`colorpicker --one-shot`

- Minden egyes kattintott képpont színének kiírása és kilépés egy billentyű lenyomásakor:

`colorpicker --quit-on-keypress`

- Csak az RGB-értéket nyomtatja ki:

`colorpicker --rgb`

- Csak a hexadecimális értéket nyomtatja ki:

`colorpicker --hex`
