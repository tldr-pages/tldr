# jpegoptim

> JPEG képek optimalizálása. További információ: <https://github.com/tjko/jpegoptim>.

- JPEG-képek optimalizálása az összes kapcsolódó adat megtartásával:

`jpegoptim {{image1.jpeg}} {{image2.jpeg}} {{imageN.jpeg}}`

- JPEG-képek optimalizálása, az összes nem lényeges adat eltávolításával:

`jpegoptim --strip-all {{image1.jpeg}} {{image2.jpeg}} {{imageN.jpeg}}`

- A kimeneti képek progresszívvá tétele:

`jpegoptim --all-progressive {{image1.jpeg}} {{image2.jpeg}} {{imageN.jpeg}}`

- A kimeneti képek maximális fájlméretének rögzítése:

`jpegoptim --size={{250k}} {{image1.jpeg}} {{image2.jpeg}} {{imageN.jpeg}}`
