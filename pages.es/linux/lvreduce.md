# lvreduce

> Reduce el tamaño de un volumen lógico.
> Vea también: `lvm`.
> Más información: <https://manned.org/lvreduce>.

- Reduce el tamaño de un volumen a 120GB:

`sudo lvreduce {{[-L|--size]}} {{120G}} {{volumen_logico}}`

- Reduce el tamaño de un volumen en 40GB así como a los sistemas subyacentes:

`sudo lvreduce {{[-L|--size]}} -{{40G}} {{[-r|--resizefs]}} {{volumen_logico}}`
