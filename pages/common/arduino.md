# arduino

> Arduino Studio - Integrated Development Environment for the Arduino platform.
> More information: <https://github.com/arduino/Arduino/blob/master/build/shared/manpage.adoc>.

- Build a sketch:

`arduino --verify {{path/to/file.ino}}`

- Build and upload a sketch:

`arduino --upload {{path/to/file.ino}}`

- Build and upload a sketch to an Arduino Nano with an Atmega328p CPU, connected on port `/dev/ttyACM0`:

`arduino --board {{arduino:avr:nano:cpu=atmega328p}} --port {{/dev/ttyACM0}} --upload {{path/to/file.ino}}`

- Set the preference `name` to a given `value`:

`arduino --pref {{name}}={{value}}`

- Build a sketch, put the build results in the build directory, and reuse any previous build results in that directory:

`arduino --pref build.path={{path/to/build_directory}} --verify {{path/to/file.ino}}`

- Save any (changed) preferences to `preferences.txt`:

`arduino --save-prefs`
