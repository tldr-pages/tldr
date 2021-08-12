# assimp

> Client de linie de comandă pentru Open Active Import Library.
> Suportă încărcarea formatelor de fișiere 3D 40+ și exportul în mai multe formate 3D populare.
> Mai multe informaţii: <http://www.assimp.org/>

- Listează toate formatele de import acceptate:

`assimp listext`

- Listează toate formatele de export acceptate:

`assimp listexport`

- Conversia unui fișier într-unul dintre formatele de ieșire acceptate, utilizând parametrii impliciți:

`assimp export {{input_file.stl}} {{output_file.obj}}`

- Conversia unui fișier folosind parametri personalizați (fișierul dox_cmd.h din codul sursă assimp listează parametrii disponibili):

`assimp export {{input_file.stl}} {{output_file.obj}} {{parameters}}`

- Afișează un rezumat al conținutului unui fișier 3D:

`assimp info {{path/to/file}}`

- Listează toate subcomenzile acceptate („verbe”):

`assimp help`

- Obțineți ajutor pentru o subcomandă specifică (de exemplu, parametrii specifici acesteia):

`assimp {{subcommand}} --help`
