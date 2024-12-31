# pamstretch

> Escala una imagen PAM interpolando entre píxeles.
> Vea también: `pamstretch-gen`, `pamenlarge`, `pamscale`.
> Más información: <https://netpbm.sourceforge.net/doc/pamstretch.html>.

- Escala una imagen PAM por un factor entero:

`pamstretch {{N}} {{ruta/a/la/imagen.pam}} > {{ruta/al/resultado.pam}}`

- Escala una imagen PAM por los factores especificados en las direcciones horizontales y verticales:

`pamstretch -xscale {{XN}} -yscale {{YN}} {{ruta/a/la/imagen.pam}} > {{ruta/al/resultado.pam}}`
