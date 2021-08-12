# lastb

> Afișează o listă a ultimilor utilizatori autentificați.

- Afișează o listă a tuturor ultimilor utilizatori autentificați:

`sudo lastb`

- Afișează o listă a tuturor ultimilor utilizatori autentificați de la un moment dat:

`sudo lastb --since {{YYYY-MM-DD}}`

- Afișează o listă a tuturor ultimilor utilizatori autentificați până la un moment dat:

`sudo lastb --until {{YYYY-MM-DD}}`

- Afișați o listă a tuturor utilizatorilor conectați la un moment dat:

`sudo lastb --present {{hh:mm}}`

- Afișați o listă a tuturor ultimilor utilizatori conectați și traduceți IP-ul într-un nume de gazdă:

`sudo lastb --dns`
