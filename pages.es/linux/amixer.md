# amixer

> Mezclador para el controlador de tarjeta de sonido ALSA.
> Más información: <https://manned.org/amixer>.

- Aumenta el volumen maestro en un 10%:

`amixer -D pulse sset Master {{10%+}}`

- Disminuye el volumen maestro en un 10%:

`amixer -D pulse sset Master {{10%-}}`
