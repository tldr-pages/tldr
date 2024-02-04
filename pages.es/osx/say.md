# say

> Convierte texto a voz.
> Más información: <https://keith.github.io/xcode-man-pages/say.1.html>.

- Di una frase en voz alta:

`say "{{Me gusta andar en mi bicicleta.}}"`

- Lee un archivo en voz alta:

`say --input-file={{nombre_de_archivo.txt}}`

- Di una frase con una voz y un ritmo de voz personalizados:

`say --voice={{voz}} --rate={{palabras_por_minuto}} "{{Lo siento David, no puedo dejarte hacer eso.}}"`

- Lista las voces disponibles (cada voz habla en un idioma distinto):

`say --voice="?"`

- Di algo en polaco:

`say --voice={{Zosia}} "{{Litwo, ojczyzno moja!}}"`

- Crea un archivo de audio con el texto hablado:

`say --output-file={{nombre_de_fichero.aiff}} "{{Aquí están los locos.}}"`
