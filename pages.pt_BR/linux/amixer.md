# amixer

> Mixer (controlador de volume) do driver de som ALSA.
> Mais informações: <https://manned.org/amixer>.

- Aumenta o volume principal em 10%:

`amixer -D pulse sset Master {{10%+}}`

- Diminui o volume principal em 10%:

`amixer -D pulse sset Master {{10%-}}`
