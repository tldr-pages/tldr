# grub-mkrescue

> Crea una imagen arrancable de GRUB para CD/USB/disquete.
> Más información: <https://www.gnu.org/software/grub/manual/grub/grub.html#Invoking-grub_002dmkrescue>.

- Crea una ISO arrancable desde el directorio actual y la guarda como `grub.iso`:

`grub-mkrescue --output {{grub.iso}} .`

- Crea una ISO usando archivos de GRUB desde un directorio personalizado:

`grub-mkrescue --directory {{/usr/lib/grub/i386-pc}} --output {{grub.iso}} {{ruta/al/origen}}`

- Usa compresión para los archivos de GRUB al construir la imagen, establecer `no` desactiva la compresión:

`grub-mkrescue --compress {{no|xz|gz|lzo}} --output {{grub.iso}} {{ruta/al/origen}}`

- Desactiva la interfaz de línea de comandos de GRUB en la imagen generada:

`grub-mkrescue --disable-cli --output {{grub.iso}} {{ruta/al/origen}}`

- Precarga módulos específicos de GRUB en la imagen:

`grub-mkrescue --modules "{{part_gpt iso9660}}" --output {{grub.iso}} {{ruta/al/origen}}`

- Pasa opciones adicionales directamente a `xorriso`:

`grub-mkrescue --output {{grub.iso}} -- {{-volid}} {{nombre_volumen}} {{ruta/al/origen}}`

- Muestra la ayuda:

`grub-mkrescue {{[-?|--help]}}`

- Muestra la versión:

`grub-mkrescue --version`
