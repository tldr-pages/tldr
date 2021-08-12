# solo

> Interacționați cu cheile de securitate hardware Solo.
> Mai multe informaţii: <https://github.com/solokeys/solo-python>

- Lista solo-uri conectate:

`solo ls`

- Actualizați firmware-ul Solo conectat în prezent la cea mai recentă versiune:

`solo key update`

- Blink condus de un anumit Solo:

`solo key wink --serial {{serial_number}}`

- Generează octeți aleatorii utilizând generatorul securizat de numere aleatorii al Solo conectat în prezent:

`solo key rng raw`

- Monitorizează ieșirea serială a unui Solo:

`solo monitor {{path/to/serial_port}}`
