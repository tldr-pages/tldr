# adscript

> Compilador de archivos Adscript.
> Más información: <https://github.com/Amplus2/Adscript>.

- Compila un archivo en un archivo objeto:

`adscript --output {{ruta/al/archivo.o}} {{ruta/al/archivo_de_entrada.adscript}}`

- Compila y vincula un archivo a un ejecutable independiente:

`adscript --executable --output {{ruta/a/archivo}} {{ruta/a/archivo_entrada.adscript}}`

- Compila un archivo a LLVM IR en lugar de código de máquina nativo:

`adscript --llvm-ir --output {{ruta/a/archivo.ll}} {{ruta/a/archivo_entrada.adscript}}`

- Crea un archivo con código objeto para otra arquitectura u otro sistema operativo:

`adscript --target-triple {{i386-linux-elf}} --output {{ruta/a/archivo.o}} {{ruta/a/archivo_entrada.adscript}}`
