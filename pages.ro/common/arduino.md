# arduino

> Arduino Studio - Mediu integrat de dezvoltare pentru platforma Arduino.
> Mai multe informaţii: <https://github.com/arduino/Arduino/blob/master/build/shared/manpage.adoc>

- Construiți o schiță:

`arduino --verify {{path/to/file.ino}}`

- Construiți și încărcați o schiță:

`arduino --upload {{path/to/file.ino}}`

- Construi și încărcați o schiță la un Arduino Nano cu un procesor ATmega328p, conectat la portul `/dev/ttyacm0`:

`arduino --board {{arduino:avr:nano:cpu=atmega328p}} --port {{/dev/ttyACM0}} --upload {{path/to/file.ino}}`

- Setați numele de preferință la o anumită `valoare':

`arduino --pref {{name}}={{value}}`

- Construiți o schiță, puneți rezultatele compilării în directorul de compilare și reutilizați rezultatele compilării anterioare din acel director:

`arduino --pref build.path={{path/to/build_directory}} --verify {{path/to/file.ino}}`

- Salvați orice preferințe (modificate) în `preferences.txt`:

`arduino --save-prefs`
