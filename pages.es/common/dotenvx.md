# dotenvx

> Un `dotenv` mejor, del creador de `dotenv`.
> Más información: <https://dotenvx.com/docs>.

- Ejecuta un comando con variables de entorno desde un archivo `.env`:

`dotenvx run -- {{comando}}`

- Ejecuta un comando con variables de entorno desde un archivo `.env` específico:

`dotenvx run -f {{ruta/al/archivo.env}} -- {{command}}`

- Establece una variable de entorno con cifrado:

`dotenvx set {{clave}} {{valor}}`

- Establece una variable de entorno sin encriptación:

`dotenvx set {{clave}} {{valor}} --plain`

- Devuelve las variables de entorno definidas en un archivo `.env`:

`dotenvx get`

- Devuelve el valor de una variable de entorno definida en un archivo `.env`:

`dotenvx get {{clave}}`

- Devuelve todas las variables de entorno de los archivos `.env` y OS:

`dotenvx get --all`
