# llvm-mc

> LLVM Machine Code Playground. Proporciona un conjunto de herramientas para trabajar con código de máquina LLVM.
> Forma parte de LLVM.
> Más información: <https://llvm.org/docs/CommandGuide/llvm-mc.html>.

- Ensambla un archivo de código ensamblador en un archivo con código de máquina:

`llvm-mc --filetype=obj -o {{ruta/a/salida.o}} {{ruta/a/entrada.s}}`

- Desensambla un archivo con código de máquina en un archivo de código ensamblador:

`llvm-mc --disassemble -o {{ruta/a/salida.s}} {{ruta/a/entrada.o}}`

- Compila el archivo de código de bits LLVM en código ensamblador:

`llvm-mc -o {{ruta/a/salida.s}} {{ruta/a/entrada.bc}}`

- Ensambla el código ensamblador desde el flujo de entrada estándar y muestra la codificación en el flujo de salida estándar:

`echo "{{addl %eax, %ebx}}" | llvm-mc -show-encoding -show-inst`

- Desensambla el código de máquina del flujo de entrada estándar para la tripleta especificada:

`echo "{{0xCD 0x21}}" | llvm-mc --disassemble -triple={{nombre_del_objetivo}}`
