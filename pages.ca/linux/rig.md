# rig

> Utilitat per generar un nom, cognom, carrer i número, en conjunt d'una ubicació geogràfica consistent (un conjunt vàlid de ciutat, estat i codi postal).
> Més informació: <https://manned.org/rig>.

- Mostra un nom aleatori (masculí o femení) i una direcció:

`rig`

- Mostra un nom [m]asculí o [f]emení aleatori i una direcció:

`rig -{{m|f}}`

- Fa servir arxius de dades d'un directori específic (per defecte és `/usr/share/rig`):

`rig -d {{ruta/al/directori}}`

- Especifica el número d'identitats a generar:

`rig -c {{numero}}`

- Especifica el número d'identitats amb el gènere escollit a generar:

`rig -{{m|f}} -c {{numero}}`
