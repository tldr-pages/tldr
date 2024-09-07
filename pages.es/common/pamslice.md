# pamslice

> Extrae una línea de valores de una imagen PAM.
> Más información: <https://netpbm.sourceforge.net/doc/pamslice.html>.

- Imprime los valores de los píxeles de la n-ésima fila en una tabla:

`pamslice -row {{n}} {{ruta/a/imagen.pam}}`

- Imprime los valores de los píxeles de la n-ésima columna de una tabla:

`pamslice -column {{n}} {{ruta/a/imagen.pam}}`

- Considera solo el m-ésimo plano de la imagen de entrada:

`pamslice -row {{n}} -plane {{m}} {{ruta/a/imagen.pam}}`

- Produce la salida en un formato adecuado para la entrada a un `xmgr` para la visualización:

`pamslice -row {{n}} -xmgr {{ruta/a/imagen.pam}}`
