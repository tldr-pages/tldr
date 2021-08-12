# i3lock

> Dulap de ecran simplu construit pentru managerul de ferestre i3.
> Mai multe informaţii: <https://i3wm.org/i3lock>

- Ecran de blocare cu un fundal simplu de culoare (format rrrggbb):

`i3lock -c {{0000ff}}`

- Blocare ecran la un fundal PNG:

`i3lock -i {{path/to/picture.png}}`

- Dezactivați indicatorul de deblocare (elimină feedback-ul la apăsarea tastaturii):

`i3lock -u`

- Afișați indicatorul mouse-ului în loc să-l ascundeți ('implicit' pentru indicatorul implicit, 'câștig' pentru un indicator MS Windows):

`i3lock -p {{default|win}}`

- Blocare ecran la un fundal PNG afișat în mai multe monitoare, cu indicatorul mouse-ului activat:

`i3lock -i {{path/to/picture.png}} -p {{default|win}} -t`
