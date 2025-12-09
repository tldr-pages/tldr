# argon2

> Calcula hashes criptográficos Argon2.
> Más información: <https://github.com/P-H-C/phc-winner-argon2#command-line-utility>.

- Calcula un hash con una contraseña y un salt con los parámetros por defecto:

`echo "{{contraseña}}" | argon2 "{{texto_salt}}"`

- Calcula un hash con el algoritmo especificado:

`echo "{{contraseña}}" | argon2 "{{texto_sal}}" -{{d|i|id}}`

- Muestra el hash de salida sin información adicional:

`echo "{{contraseña}}" | argon2 "{{texto_sal}}" -e`

- Calcula un hash con una cantidad de i[t]eraciones dada, uso de [m]emoria y parámetros de [p]aralelismo dados:

`echo "{{contraseña}}" | argon2 "{{texto_sal}}" -t {{5}} -m {{20}} -p {{7}}`
