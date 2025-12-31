# pamflip

> Refleja o gira una imagen PAM o PNM.
> Más información: <https://netpbm.sourceforge.net/doc/pamflip.html>.

- Gira la imagen de entrada en sentido contrario a las manecillas del reloj una cantidad de grados específica:

`pamflip {{[-r|-rotate]}}{{90|180|270}} {{ruta/a/la/entrada.pam}} > {{ruta/al/resultado.pam}}`

- Refleja horizontalmente:

`pamflip {{[-lr|-leftright]}} {{ruta/a/la/entrada.pam}} > {{ruta/al/resultado.pam}}`

- Refleja verticalmente:

`pamflip {{[-tb|-topbottom]}} {{ruta/a/la/entrada.pam}} > {{ruta/al/resultado.pam}}`

- Refleja la imagen de entrada por la diagonal principal:

`pamflip {{[-xy|-transpose]}} {{ruta/a/la/entrada.pam}} > {{ruta/al/resultado.pam}}`
