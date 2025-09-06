# apg

> Crea contraseñas aleatorias arbitrariamente complejas.
> Más información: <https://manned.org/apg>.

- Crea contraseñas aleatorias (la longitud predeterminada de la contraseña es 8):

`apg`

- Crea una contraseña con al menos 1 símbolo (S), 1 número (N), 1 mayúscula (C), 1 minúscula (L):

`apg -M SNCL`

- Crea una contraseña con 16 caracteres:

`apg -m {{16}}`

- Crea una contraseña con una longitud máxima de 16:

`apg -x {{16}}`

- Crea una contraseña que no aparece en un diccionario (se debe proporcionar el archivo del diccionario):

`apg -r {{ruta/al/archivo_diccionario}}`
