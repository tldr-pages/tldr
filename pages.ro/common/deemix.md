# deemix

> O bibliotecă descendentă deezer deezer construit din cenușa Deezloader Remix.
> Acesta poate fi folosit ca o aplicație CLI independentă sau implementat într-o interfață cu utilizatorul utilizând API.
> Mai multe informaţii: <https://deemix.app>

- Descărcați o piesă sau o listă de redare:

`deemix {{https://www.deezer.com/us/track/00000000}}`

- Descărcați pista/lista de redare la o anumită rată de biți:

`deemix --bitrate {{FLAC|MP3}} {{url}}`

- Descărcați pe o anumită cale:

`deemix --bitrate {{bitrate}} --path {{path}} {{url}}`

- Creați un deemix config portabil în directorul curent:

`deemix --portable --bitrate {{bitrate}} --path {{path}} {{url}}`
