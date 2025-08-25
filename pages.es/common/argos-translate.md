# argos-translate

> Una biblioteca de traducción local (offline) de código abierto y una herramienta CLI escrita en Python.
> Más información: <https://argos-translate.readthedocs.io/en/latest/source/cli.html>.

- Instala pares de traducción del español al inglés:

`argospm install translate-es_en`

- Traduce un texto del español (`es`) al inglés (`en`) (Nota: sólo se admiten códigos de dos letras para los idiomas:

`argos-translate --from-lang es --to-lang en {{un texto corto}}`

- Traduce un archivo de texto del inglés al hindi:

`cat {{ruta/al/archivo.txt}} | argos-translate --from-lang en --to-lang hi`

- Lista todos los pares de traducción instalados:

`argospm list`

- Muestra pares de traducción del inglés que están disponibles para ser instalados:

`argospm search --from-lang en`

- Actualiza pares de paquetes de lenguaje instalados:

`argospm update`

- Traduce de `ar` a `ru` (Nota: esto requiere que se instalen los pares de traducción `translate-ar_en` y `translate-en_ru`):

`argos-translate --from-lang ar --to-lang ru {{صورة تساوي أكثر من ألف كلمة}}`
