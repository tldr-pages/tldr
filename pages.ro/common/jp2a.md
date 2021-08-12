# jp2a

> Conversia imaginilor JPEG în ASCII.
> Mai multe informaţii: <https://csl.name/jp2a/>

- Citiți imaginea JPEG dintr-un fișier și imprimați în ASCII:

`jp2a {{path/to/image.jpeg}}`

- Citiți imaginea JPEG de la un URL și imprimați în ASCII:

`jp2a {{www.example.com/image.jpeg}}`

- Colorizează ieșirea ASCII:

`jp2a --colors {{path/to/image.jpeg}}`

- Specificați caracterele care urmează să fie utilizate pentru ieșirea ASCII:

`jp2a --chars='{{..-ooxx@@}}' {{path/to/image.jpeg}}`

- Scrieți ieșirea ASCII într-un fișier:

`jp2a --output={{path/to/output_file.txt}} {{path/to/image.jpeg}}`

- Scrieți ieșirea ASCII în format de fișier HTML, potrivit pentru vizualizarea în browsere web:

`jp2a --html --output={{path/to/output_file.html}} {{path/to/image.jpeg}}`
