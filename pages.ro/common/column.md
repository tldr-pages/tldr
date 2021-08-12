# column

> Formatați intrarea standard sau un fișier în mai multe coloane.
> Coloanele sunt completate înaintea rândurilor; separatorul implicit este un spațiu alb.
> Mai multe informaţii: <https://manned.org/column>

- Formatarea ieșirii unei comenzi pentru un afișaj lat de 30 de caractere:

`printf "header1 header2\nbar foo\n" | column --output-width {{30}}`

- Divizarea automată a coloanelor și alinierea automată a acestora într-un format tabelar:

`printf "header1 header2\nbar foo\n" | column --table`

- Specificați caracterul delimitator de coloană pentru opțiunea `—table' (de exemplu „,” pentru csv) (valori implicite în spațiu alb):

`printf "header1,header2\nbar,foo\n" | column --table --separator {{,}}`

- Umpleți rândurile înainte de completarea coloanelor:

`printf "header1\nbar\nfoobar\n" | column --output-width {{30}} --fillrows`
