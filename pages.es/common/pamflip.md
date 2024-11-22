# pamflip

> Refleja o gira una imagen PAM o PNM.
> Más información: <https://netpbm.sourceforge.net/doc/pamflip.html>.

- Gira la imagen de entrada en sentido contrario a las manecillas del reloj una cantidad de grados específica:

`pamflip -rotate{{90|180|270}} {{ruta/a/la/entrada.pam}} > {{ruta/al/resultado.pam}}`

- Refleja horizontalmente:

`pamflip -leftright {{ruta/a/la/entrada.pam}} > {{ruta/al/resultado.pam}}`

- Refleja verticalmente:

`pamflip -topbottom {{ruta/a/la/entrada.pam}} > {{ruta/al/resultado.pam}}`

- Refleja la imagen de entrada por la diagonal principal:

`pamflip -transpose {{ruta/a/la/entrada.pam}} > {{ruta/al/resultado.pam}}`
