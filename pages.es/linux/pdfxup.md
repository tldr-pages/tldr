# pdfxup

> N-up páginas PDF.
> N-upping significa poner múltiples páginas en una página escalando y rotándolas en una cuadrícula.
> Más información: <https://ctan.org/pkg/pdfxup>.

- Crea un 2-up PDF:

`pdfxup -o {{ruta/al/resultado.pdf}} {{ruta/a/la/entrada.pdf}}`

- Crea un PDF con 3 columnas y 2 líneas por página:

`pdfxup -x {{3}} -y {{2}} -o {{ruta/al/resultado.pdf}} {{ruta/a/la/entrada.pdf}}`

- Crea un PDF en modo cuadernillo (2-up, y las páginas se ordenan para formar un libro cuando se doblan):

`pdfxup -b -o {{ruta/al/resultado.pdf}} {{ruta/a/la/entrada.pdf}}`
