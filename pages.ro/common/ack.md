# ack

> Un instrument de căutare precum grep, optimizat pentru dezvoltatori.
> A se vedea, de asemenea,: `rg`, care este mult mai rapid.
> Mai multe informaţii: <https://beyondgrep.com/documentation>

- Căutați fișiere care conțin un șir sau o expresie regulată în directorul curent recursiv:

`ack "{{search_pattern}}"`

- Caută un model insensibil la majuscule:

`ack --ignore-case "{{search_pattern}}"`

- Căutați linii care se potrivesc unui model, tipăriți [o] nly textul potrivit și nu restul liniei:

`ack -o "{{search_pattern}}"`

- Limitați căutarea la fișiere de un anumit tip:

`ack --type={{ruby}} "{{search_pattern}}`

- Nu căutați în fișiere de un anumit tip:

`ack --type=no{{ruby}} "{{search_pattern}}`

- Numără numărul total de meciuri găsite:

`ack --count --no-filename "{{search_pattern}}"`

- Imprimați numele fișierelor și numărul de potriviri numai pentru fiecare fișier:

`ack --count --files-with-matches "{{search_pattern}}"`

- Listează toate valorile care pot fi utilizate cu `—type`:

`ack --help-types`
