# pwn

> Biblioteca de desarrollo de exploits diseñada para la creación rápida de prototipos.
> Más información: <https://docs.pwntools.com/en/stable/commandline.html>.

- Convierte el código ensamblador dado a `bytes`:

`pwn asm "{{xor edi, edi}}"`

- Crea un patrón cíclico dado un número específico de caracteres:

`pwn cyclic {{número}}`

- Codifica los datos dados en el sistema hexadecimal:

`pwn hex {{deafbeef}}`

- Decodifica los datos dados en hexadecimal:

`pwn unhex {{6c4f7645}}`

- Imprime un shellcode de Linux x64 para ejecutar un intérprete de comandos:

`pwn shellcraft {{amd64.linux.sh}}`

- Comprueba la configuración de seguridad binaria para el archivo ELF dado:

`pwn checksec {{ruta/al/archivo}}`

- Busca actualizaciones de Pwntools:

`pwn update`

- Muestra versión:

`pwn version`
