# lvextend

> Aumenta el tamaño de un volumen lógico.
> Vea tambien: `lvm`.
> Más información: <https://manned.org/lvextend.8>.

- Aumenta el tamaño de un volumen a 120 GB:

`sudo lvextend {{[-L|--size]}} {{120G}} {{volumen_logico}}`

- Aumenta el tamaño de un volumen por 40 GB, así como a los sistemas subyacentes:

`sudo lvextend {{[-L|--size]}} +{{40G}} {{[-r|--resizefs]}} {{volumen_logico}}`

- Aumenta el tamaño de un volumen al 100% del espacio físico libre del volumen:

`sudo lvextend {{[-l|--extents]}} +{{100}}%FREE {{volumen_logico}}`

- Aumenta el tamaño de un volumen al 100% del espacio físico libre del volumen y redimensiona a los sistemas subyacentes:

`sudo lvextend {{[-l|--extents]}} +{{100}}%FREE {{[-r|--resizefs]}} {{volumen_logico}}`
