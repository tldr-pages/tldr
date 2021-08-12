# faketime

> Falsifica timpul de sistem pentru o anumită comandă.
> Mai multe informaţii: <https://manpages.ubuntu.com/manpages/trusty/man1/faketime.1.html>

- Falsifică ora până în această seară, înainte de tipărirea rezultatului `date`:

`faketime '{{today 23:30}}' {{date}}`

- Deschideți un nou shell `bash`, care utilizează ieri ca dată curentă:

`faketime '{{yesterday}}' {{bash}}`

- Simulează modul în care orice program ar acționa vinerea viitoare:

`faketime '{{next Friday 1 am}}' {{path/to/any/program}}`
