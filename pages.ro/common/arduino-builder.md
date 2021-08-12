# arduino-builder

> Un instrument de linie de comandă pentru compilarea schițe arduino.
> ÎNVECHIRE AVERTISMENT: Acest instrument este eliminat treptat în favoarea `arduino`.
> Mai multe informaţii: <https://github.com/arduino/arduino-builder>

- Compilați o schiță:

`arduino-builder -compile {{path/to/sketch.ino}}`

- Specificați nivelul de depanare (1 la 10, valorile implicite la 5):

`arduino-builder -debug-level {{level}}`

- Specificați un director personalizat de compilare:

`arduino-builder -build-path {{path/to/build_directory}}`

- Utilizați un fișier de opțiune de compilare, în loc să specificați manual `—hardware`, `—tools` etc. de fiecare dată:

`arduino-builder -build-options-file {{path/to/build.options.json}}`

- Activează modul verbose:

`arduino-builder -verbose {{true}}`
