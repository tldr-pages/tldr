# grub-mkconfig

> Generar un archivo de configuracion de GRUB.
> Más información: <https://www.gnu.org/software/grub/manual/grub/html_node/Invoking-grub_002dmkconfig.html>.

- Ejecutar el comando solo e imprimir la salida a `stdout`:

`sudo grub-mkconfig`

- Generar el archivo de configuracion:

`sudo grub-mkconfig --output={{/boot/grub/grub.cfg}}`

- Imprimir la pagina de ayuda:

`grub-mkconfig --help`
