# brightnessctl

> Utilidad para leer y controlar el brillo de dispositivos en sistemas operativos Linux.
> Más información: <https://github.com/Hummer12007/brightnessctl#usage>.

- Lista de dispositivos a los que se les puede cambiar el brillo:

`brightnessctl {{[-l|--list]}}`

- Imprime el brillo actual de la luz trasera de la pantalla:

`brightnessctl get`

- Establece el brillo de la luz trasera de la pantalla a un porcentaje en el rango válido:

`brightnessctl set {{50%}}`

- Aumenta el brillo con un incremento específico:

`brightnessctl set {{+10%}}`

- Disminuye el brillo con un decremento específico:

`brightnessctl set {{10%-}}`
