# printf

> Formatea e imprime texto.
> Vea también: `echo`.
> Más información: <https://www.gnu.org/software/coreutils/manual/html_node/printf-invocation.html>.

- Imprime un mensaje de texto:

`printf "{{%s\n}}" "{{Hola mundo}}"`

- Imprime un número entero en negrita azul:

`printf "{{\e[1;34m%.3d\e[0m\n}}" {{42}}`

- Imprime un número flotante con el signo del euro Unicode:

`printf "{{\u20AC %.2f\n}}" {{123.4}}`

- Imprime un mensaje de texto compuesto con variables de entorno:

`printf "{{var1: %s\tvar2: %s\n}}" "{{$VAR1}}" "{{$VAR2}}"`

- Almacena un mensaje formateado en una variable (no funciona en Zsh):

`printf -v {{myvar}} {{"Esto es %s = %d\n" "un año" 2016}}`

- Imprime un número hexadecimal, octal y científico:

`printf "{{hex=%x octal=%o scientific=%e\n}}" 0x{{FF}} 0{{377}} {{100000}}`
