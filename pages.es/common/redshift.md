# redshift

> Ajusta la temperatura de color de una pantalla en función de su entorno.
> Nota: Redshift no es compatible con Wayland.
> Vea también: `gammastep`.
> Más información: <https://manned.org/redshift>.

- Activa Redshift con la [t]emperatura ajustada a 5700k durante el día y a 3600k por la noche:

`redshift -t 5700:3600`

- Activa Redshift con una [l]ocalización personalizada especificada manualmente:

`redshift -l {{latitud}}:{{longitud}}`

- Activa Redshift con el [b]rillo de la pantalla ajustado al 70% durante el día y al 40% por la noche:

`redshift -b 0.7:0.4`

- Activa Redshift con niveles de [g]amma personalizados (entre 0 y 1):

`redshift -g {{red}}:{{green}}:{{blue}}`

- [P]urga los cambios de temperatura existentes y establece una temperatura de color constante e inalterable en modo [O]ne-shot:

`redshift -PO {{temperatura}}`
