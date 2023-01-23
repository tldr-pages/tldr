# arduino

> Arduino Studio - Integrált fejlesztőkörnyezet az Arduino platformhoz. További információ: <https://github.com/arduino/Arduino/blob/master/build/shared/manpage.adoc>.

- Készítsen egy vázlatot:

`arduino --verify {{path/to/file.ino}}`

- Építsen és töltsön fel egy vázlatot:

`arduino --upload {{path/to/file.ino}}`

- Építsen és töltsön fel egy vázlatot egy Arduino Nano Atmega328p CPU-val, csatlakoztatva a `/dev/ttyACM0` porton :

`arduino --board {{arduino:avr:nano:cpu=atmega328p}} --port {{/dev/ttyACM0}} --upload {{path/to/file.ino}}`

- Állítsa be a preferenciát `name` egy adott `value`:

`arduino --pref {{name}}={{value}}`

- Építsen egy vázlatot, tegye a build eredményeit a build könyvtárba, és használja újra a korábbi build eredményeket ebben a könyvtárban:

`arduino --pref build.path={{path/to/build_directory}} --verify {{path/to/file.ino}}`

- Mentse el az összes (módosított) preferenciát a `preferences.txt`:

`arduino --save-prefs`

- Telepítse a legújabb SAM kártyát:

`arduino --install-boards "{{arduino:sam}}"`

- Telepítse a Bridge és Servo könyvtárakat:

`arduino --install-library "{{Bridge:1.0.0,Servo:1.2.0}}"`
