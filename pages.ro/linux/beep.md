# beep

> Un utilitar pentru a emite un semnal sonor al PC-ului.
> Mai multe informaţii: <https://github.com/spkr-beep/beep>

- Cântă un bip:

`beep`

- Redați un semnal sonor care se repetă:

`beep -r {{repetitions}}`

- Redați un semnal sonor la o frecvență specificată (Hz) și durată (milisecunde):

`beep -f {{frequency}} -l {{duration}}`

- Redați fiecare frecvență nouă și durată ca un semnal sonor distinct:

`beep -f {{frequency}} -l {{duration}} -n -f {{frequency}} -l {{duration}}`

- Joaca scara C majore:

`beep -f 262 -n -f 294 -n -f 330 -n -f 349 -n -f 392 -n -f 440 -n -f 494 -n -f 523`
