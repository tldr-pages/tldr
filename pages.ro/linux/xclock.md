# xclock

> Afișați ora în formă analogică sau digitală.

- Afișează un ceas analogic:

`xclock`

- Afișează un ceas digital de 24 de ore cu câmpurile de oră și minut numai:

`xclock -digital -brief`

- Afișează un ceas digital folosind un șir de format strftime (vezi strftime (3)):

`xclock -digital -strftime {{format}}`

- Afișați un ceas digital de 24 de ore cu câmpurile de oră, minut și al doilea care actualizează fiecare secundă:

`xclock -digital -strftime '%H:%M:%S' -update 1`

- Afișează un ceas digital de 12 ore cu câmpurile de oră și minut:

`xclock -digital -twelve -brief`
