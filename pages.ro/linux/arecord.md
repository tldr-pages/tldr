# arecord

> Înregistrator de sunet pentru driverul de placă de sunet ALSA.
> Mai multe informaţii: <https://manned.org/arecord>

- Înregistrați un fragment în calitate „CD” (terminați cu Ctrl-C când ați terminat):

`arecord -vv --format=cd {{path/to/file.wav}}`

- Înregistrați un fragment în calitate „CD”, cu o durată fixă de 10 secunde:

`arecord -vv --format=cd --duration={{10}} {{path/to/file.wav}}`

- Înregistrați un fragment și salvați-l ca mp3 (terminați cu Ctrl-C când ați terminat):

`arecord -vv --format=cd --file-type raw | lame -r - {{path/to/file.mp3}}`

- Listează toate plăcile de sunet și dispozitivele audio digitale:

`arecord --list-devices`

- Permite interfața interactivă (de exemplu, utilizați bara spațială sau introduceți pentru a juca sau pauză):

`arecord --interactive`
