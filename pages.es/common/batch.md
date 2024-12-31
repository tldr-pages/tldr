# batch

> Ejecuta comandos en un momento posterior cuando los niveles de carga del sistema lo permitan.
> Los resultados serán enviados al correo del usuario.
> Vea también: `at`, `atq`, `atrm` `mail`.
> Más información: <https://manned.org/batch>.

- Lanza el servicio `atd`:

`systemctl start atd`

- Ejecuta comandos de `stdin` (presiona `Ctrl + D` cuando hayas finalizado):

`batch`

- Ejecuta un comando desde `stdin`:

`echo "{{./hacer_copia_de_la_bd.sh}}" | batch`
