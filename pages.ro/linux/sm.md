# sm

> Afișează un mesaj scurt ecran complet.
> Mai multe informaţii: <https://github.com/nomeata/screen-message>

- Afișează un mesaj pe ecran complet:

`sm "{{Hello World!}}"`

- Afișează un mesaj cu culori inversate:

`sm -i "{{Hello World!}}"`

- Afișează un mesaj cu o culoare personalizată de prim-plan:

`sm -f {{blue}} "{{Hello World!}}"`

- Afișarea unui mesaj cu o culoare de fundal personalizată:

`sm -b {{#008888}} "{{Hello World!}}"`

- Afișează un mesaj rotit de 3 ori (în pași de 90 de grade, în sens invers acelor de ceasornic):

`sm -r {{3}} "{{Hello World!}}"`

- Afișează un mesaj utilizând ieșirea dintr-o altă comandă:

`{{echo "Hello World!"}} | sm -`
