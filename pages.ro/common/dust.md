# dust

> Praf oferă o imagine de ansamblu instantanee a directoarelor care utilizează spațiu pe disc.
> Mai multe informaţii: <https://github.com/bootandy/dust>

- Afișează informații pentru directorul curent:

`dust`

- Afișează informații pentru o listă de directoare separate de spațiu:

`dust {{path/to/directory1}} {{path/to/directory2}}`

- Afișează 30 de directoare (implicit la 21):

`dust --number-of-lines {{30}}`

- Afiseaza informatii pentru directorul curent, pana la 3 nivele adancime:

`dust --depth {{3}}`

- Afișează cele mai mari directoare din partea de sus în ordine descrescătoare:

`dust --reverse`

- Ignorați toate fișierele și directoarele cu un anumit nume:

`dust --ignore-directory {{file_or_directory_name}}`

- Nu afișați procente de bare și procente:

`dust --no-percent-bars`
