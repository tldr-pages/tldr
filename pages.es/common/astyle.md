# astyle

> Indentador, formateador y embellecedor de código fuente para los lenguajes de programación C, C++, C# y Java.
> Al ejecutarse, se crea una copia del archivo original con un ".orig" añadido al nombre del archivo original.
> Más información: <https://manned.org/astyle>.

- Aplica el estilo por defecto de 4 espacios por sangría y sin cambios de formato:

`astyle {{archivo_de_origen}}`

- Aplica el estilo Java con llaves adjuntas:

`astyle {{[-A2|--style=java]}} {{ruta/al/archivo}}`

- Aplica el estilo allman con llaves discontinuas:

`astyle {{[-A1|--style=allman]}} {{ruta/al/archivo}}`

- Aplica una sangría personalizada utilizando espacios. Elige entre 2 y 20 espacios:

`astyle {{[-s|--indent=spaces=]}}{{número_de_espacios}} {{ruta/al/archivo}}`

- Aplica una sangría personalizada utilizando tabuladores. Elige entre 2 y 20 tabulaciones:

`astyle {{[-t|--indent=tab=]}{{número_de_pestañas}} {{ruta/al/archivo}}`
