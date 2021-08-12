# nano

> Editor text simplu, ușor de utilizat în linia de comandă. O clonă Pico îmbunătățită, gratuită.
> Mai multe informaţii: <https://nano-editor.org>

- Deschideți un fișier nou în nano:

`nano`

- Deschideţi un anumit fişier:

`nano {{path/to/file}}`

- Deschideți un anumit fișier, poziționând cursorul la linia și coloana specificată:

`nano +{{line}},{{column}} {{path/to/file}}`

- Deschideți un anumit fișier și activați ambalarea moale:

`nano --softwrap {{path/to/file}}`

- Deschideți un anumit fișier și indentați linii noi la indentarea liniilor anterioare:

`nano --autoindent {{path/to/file}}`

- Deschideţi nano şi creaţi un fişier de rezervă (`file~`) când salvaţi editările:

`nano --backup {{path/to/file}}`
