# dmenu

> Meniu dinamic.
> Creează un meniu dintr-o intrare de text cu fiecare element dintr-o linie nouă.
> Mai multe informaţii: <https://manned.org/dmenu>

- Afișează un meniu al ieșirii comenzii `ls`:

`{{ls}} | dmenu`

- Afișează un meniu cu elemente personalizate separate printr-o linie nouă (`\ n`):

`echo -e "{{red}}\n{{green}}\n{{blue}}" | dmenu`

- Lăsați utilizatorul să aleagă între mai multe elemente și să salveze pe cel selectat într-un fișier:

`echo -e "{{red}}\n{{green}}\n{{blue}}" | dmenu > {{color.txt}}`

- Lansarea dmenu pe un anumit monitor:

`ls | dmenu -m {{1}}`

- Afișează dmenu în partea de jos a ecranului:

`ls | dmenu -b`
