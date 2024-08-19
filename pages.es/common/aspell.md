# aspell

> Corrector ortográfico interactivo.
> Más información: <http://aspell.net/>.

- Revisa la ortografía de un solo archivo:

`aspell check {{ruta/al/archivo}}`

- Lista las palabras mal escritas de `stdin`:

`cat {{ruta/a/archivo}} | aspell list`

- Muestra los idiomas disponibles en el diccionario:

`aspell dicts`

- Ejecuta `aspell` con un idioma diferente (toma el código de idioma ISO 639 de dos letras):

`aspell --lang={{cs}}`

- Lista las palabras mal escritas de `stdin` e ignora las palabras de la lista personal de palabras:

`cat {{ruta/a/archivo}} | aspell --personal={{lista-personal-de-palabras.pws}} list`
