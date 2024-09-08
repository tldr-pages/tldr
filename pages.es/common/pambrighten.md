# pambrighten

> Cambia la saturación y el valor de una imagen PAM.
> Más información: <https://netpbm.sourceforge.net/doc/pambrighten.html>.

- Aumenta la saturación de cada píxel con un porcentaje específico:

`pambrighten -saturation {{valor_porcentual}} {{ruta/a/imagen.pam}} > {{ruta/a/archivo_de_salida.pam}}`

- Aumenta el valor (del espacio de color HSV) de cada píxel con un porcentaje específico:

`pambrighten -value {{valor_porcentual}} {{ruta/a/imagen.pam}} > {{ruta/a/archivo_de_salida.pam}}`
