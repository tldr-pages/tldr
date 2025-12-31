# znc

> Rebotador de IRC.
> Más información: <https://manned.org/znc>.

- Ejecuta la configuración inicial:

`znc {{[-c|--makeconf]}}`

- Inicia el programa residente del rebotador de IRC:

`znc`

- Configura `znc` para systemd:

`sudo {{[-u|--user]}} znc znc {{[-c|--makeconf]}} {{[-d|--datadir]}} /var/lib/znc`

- Habilita `znc` para que se inicie desde el inicio:

`systemctl enable znc --now`
