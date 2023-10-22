# adscript

> Compilador de archivos Adscript.
> Más información: <https://github.com/Amplus2/Adscript>.

- Compilar un archivo en un archivo objeto:

`adscript --output {{ruta/al/archivo.o}} {{ruta/al/archivo_de_entrada.adscript}}`

- Compilar y vincular un archivo a un ejecutable independiente:

`adscript --executable --output {{ruta/a/archivo}} {{ruta/a/archivo_entrada.adscript}}`

- Compilar un archivo a LLVM IR en lugar de código de máquina nativo:

`adscript --llvm-ir --output {{ruta/a/archivo.ll}} {{ruta/a/archivo_entrada.adscript}}`

- Compilación cruzada de un archivo a un archivo objeto para una arquitectura de CPU o un sistema operativo foráneo:

`adscript --target-triple {{i386-linux-elf}} --output {{ruta/a/archivo.o}} {{ruta/a/archivo_entrada.adscript}}`
