# lvresize

> Cambia el tamaño de un volumen lógico.
> Vea también: `lvm`.
> Más información: <https://manned.org/lvresize>.

- Cambia el tamaño de un volumen lógico a 120 GB:

`lvresize --size {{120G}} {{grupo_de_volumen}}/{{volumen_logico}}`

- Extiende el tamaño de un volumen lógico así como el de los sistemas subyacentes en 120 GB:

`lvresize --size +{{120G}} --resizefs {{grupo_de_volumen}}/{{volumen_logico}}`

- Extiende el tamaño de un volumen lógico al 100% del espacio físico libre del volumen:

`lvresize --size {{100}}%FREE {{grupo_de_volumen}}/{{volumen_logico}}`

- Reduce el tamaño de un volumen lógico así como a los sistemas subyacentes en 120 GB:

`lvresize --size -{{120G}} --resizefs {{grupo_de_volumen}}/{{volumen_logico}}`
