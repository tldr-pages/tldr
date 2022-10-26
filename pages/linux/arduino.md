# arduino

> Integrated development environment for Arduino boards.
> More information: <https://manned.org/arduino>.

- Start the Arduino IDE, with two files open:

`arduino {{path/to/file1}} {{path/to/file2}}`

- Compile and upload a sketch using the last selected board and serial port:

`arduino --upload {{path/to/file}}`

- Install latest SAM board support:

`arduino --install-boards "arduino:sam"`

- Change the selected board and build path and do nothing else:

`arduino --pref build.path={{/path/to/sketch/build}} --board arduino:avr:uno --save-prefs`

- Install Bridge and Servo libraries:

`arduino --install-library "Bridge:1.0.0,Servo:1.2.0"`

- Compile and upload a sketch to an Arduino Nano, with an Atmega168 CPU, connected on port /dev/ttyACM0:

`arduino --board arduino:avr:nano:cpu=atmega168 --port /dev/ttyACM0 --upload {{/path/to/file}}`
