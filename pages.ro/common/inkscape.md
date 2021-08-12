# inkscape

> Un program de editare SVG (Scalable Vector Graphics).
> Pentru versiunile Inkscape de până la 0.92.x, utilizați -e în loc de -o.
> Mai multe informaţii: <https://inkscape.org>

- Deschideți un fișier SVG în GUI Inkscape:

`inkscape {{filename.svg}}`

- Exportați un fișier SVG într-un bitmap cu formatul implicit (PNG) și rezoluția implicită (96 DPI):

`inkscape {{filename.svg}} -o {{filename.png}}`

- Exportați un fișier SVG într-un bitmap de 600x400 pixeli (pot apărea distorsiuni ale raportului de aspect):

`inkscape {{filename.svg}} -o {{filename.png}} -w {{600}} -h {{400}}`

- Exportaţi desenul (caseta de încadrare a tuturor obiectelor) al unui fişier SVG într-un bitmap:

`inkscape {{filename.svg}} -o {{filename.png}} -D`

- Exportați un singur obiect, având în vedere ID-ul său, într-un bitmap:

`inkscape {{filename.svg}} -i {{id}} -o {{object.png}}`

- Exportați un document SVG în PDF, convertiți toate textele în căi:

`inkscape {{filename.svg}} -o {{filename.pdf}} --export-text-to-path`

- Duplicați obiectul cu id="path123", rotiți dublul 90 de grade, salvați fișierul și ieșiți din Inkscape:

`inkscape {{filename.svg}} --select=path123 --verb="{{EditDuplicate;ObjectRotate90;FileSave;FileQuit}}"`
