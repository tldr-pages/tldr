# gource

> Redă o diagramă animată a depozitelor Git, SVN, Mercurial și Bazaar.
> Afișează fișierele și directoarele create, modificate sau eliminate în timp.
> Mai multe informaţii: <https://gource.io>

- Rulați gource într-un director (dacă nu este directorul rădăcină al depozitului, rădăcina este căutată de acolo):

`gource {{path/to/repository}}`

- Rulați gource în directorul curent, cu o rezoluție personalizată de ieșire:

`gource -{{width}}x{{height}}`

- Setați o scală de timp personalizată pentru animație:

`gource -c {{time_scale_multiplier}}`

- Setați cât de mult ar trebui să fie în fiecare zi în animație (acest lucru se combină cu -c, dacă este prevăzut):

`gource -s {{seconds}}`

- Setați modul ecran complet și o culoare de fundal personalizată:

`gource -f -b {{hex_color_code}}`

- Stabilește un titlu pentru animație:

`gource --title {{title}}`
