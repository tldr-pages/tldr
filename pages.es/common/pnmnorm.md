# pnmnorm

> Normaliza el contraste en una imagen PNM.
> Vea también: `pnmhisteq`.
> Más información: <https://netpbm.sourceforge.net/doc/pnmnorm.html>.

- Fuerza los píxeles más brillantes a ser blancos, los más oscuros hacia negro y disemina los demás linealmente:

`pnmnorm {{ruta/a/la/imagen.pnm}} > {{ruta/al/resultado.pnm}}`

- Fuerza los píxeles más brillantes a ser blancos, los más oscuros hacia negro y disemina los demás cuadráticamente, de tal forma que los píxeles con un brillo de 'n' tienen un 50 % del brillo:

`pnmnorm -midvalue {{n}} {{ruta/a/la/imagen.pnm}} > {{ruta/al/resultado.pnm}}`

- Mantiene el tono (hue) de los píxeles, solo modifica el brillo:

`pnmnorm -keephues {{ruta/a/la/imagen.pnm}} > {{ruta/al/resultado.pnm}}`

- Especifica un método para calcular el brillo de un píxel:

`pnmnorm -{{luminosity|colorvalue|saturation}} {{ruta/a/la/imagen.pnm}} > {{ruta/al/resultado.pnm}}`
