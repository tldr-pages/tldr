# pwn

> Biblioteca de desarrollo de exploits diseñada para la creación rápida de prototipos.
> Más información: <https://docs.pwntools.com/en/stable/commandline.html>.

- Convierte código ensamblador a `bytes`:

`pwn asm "{{xor edi, edi}}"`

- Crea un patrón cíclico con un número específico de caracteres:

`pwn cyclic {{número}}`

- Codifica datos en el sistema hexadecimal:

`pwn hex {{deafbeef}}`

- Decodifica datos en hexadecimal:

`pwn unhex {{6c4f7645}}`

- Imprime código de intérprete de Linux x64 para ejecutar en un intérprete:

`pwn shellcraft {{amd64.linux.sh}}`

- Comprueba la configuración de seguridad binaria del archivo ELF dado:

`pwn checksec {{ruta/al/archivo}}`

- Busca actualizaciones de Pwntools:

`pwn update`

- Muestra la versión:

`pwn version`
