# trans

> Translate Shell es un traductor de línea de comandos.
> Más información: <https://github.com/soimort/translate-shell>.

- Traduce una palabra (el idioma es detectado automáticamente):

`trans "{{palabra_u_oración_a_traducir}}"`

- Genera una traducción corta:

`trans --brief "{{palabra_u_oración_a_traducir}}"`

- Traduce una palabra al español:

`trans :{{es}} {{palabra}}`

- Traduce una palabra del alemán al español:

`trans {{de}}:{{es}} {{Schmetterling}}`

- Se comporta como un diccionario para obtener el significado de una palabra:

`trans -d {{palabra}}`
