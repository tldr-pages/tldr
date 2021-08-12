# jpegoptim

> Optimizați imaginile JPEG.
> Mai multe informaţii: <https://github.com/tjko/jpegoptim>

- Optimizarea unui set de imagini JPEG, păstrând toate datele asociate:

`jpegoptim {{image1.jpeg}} {{image2.jpeg}} {{imageN.jpeg}}`

- Optimizarea imaginilor JPEG, dezmembrarea tuturor datelor neesenţiale:

`jpegoptim --strip-all {{image1.jpeg}} {{image2.jpeg}} {{imageN.jpeg}}`

- Forțați imaginile de ieșire să fie progresive:

`jpegoptim --all-progressive {{image1.jpeg}} {{image2.jpeg}} {{imageN.jpeg}}`

- Forțați imaginile de ieșire să aibă o dimensiune maximă fixă a fișierului:

`jpegoptim --size={{250k}} {{image1.jpeg}} {{image2.jpeg}} {{imageN.jpeg}}`
