# arduino

> Arduino Studio - Ինտեգրված զարգացման միջավայր Arduino հարթակի համար:.
> Լրացուցիչ տեղեկություններ. <https://github.com/arduino/Arduino/blob/master/build/shared/manpage.adoc>:.

- Կառուցեք ուրվագիծ.:

`arduino --verify {{path/to/file.ino}}`

- Կառուցեք և վերբեռնեք էսքիզ.:

`arduino --upload {{path/to/file.ino}}`

- Ստեղծեք և վերբեռնեք էսքիզ Arduino Nano-ում Atmega328p պրոցեսորով, որը միացված է `/dev/ttyACM0` նավահանգստին:

`arduino --board {{arduino:avr:nano:cpu=atmega328p}} --port {{/dev/ttyACM0}} --upload {{path/to/file.ino}}`

- Սահմանեք `name` նախապատվությունը տրված `value`-ին:

`arduino --pref {{name}}={{value}}`

- Կառուցեք ուրվագիծ, տեղադրեք կառուցման արդյունքները build գրացուցակում և վերօգտագործեք ցանկացած նախորդ կառուցման արդյունքներ այդ գրացուցակում.:

`arduino --pref build.path={{path/to/build_directory}} --verify {{path/to/file.ino}}`

- Պահպանեք ցանկացած (փոփոխված) նախապատվություն `preferences.txt`-ում՝:

`arduino --save-prefs`

- Տեղադրեք վերջին SAM տախտակը.:

`arduino --install-boards "{{arduino:sam}}"`

- Տեղադրեք Bridge և Servo գրադարանները.:

`arduino --install-library "{{Bridge:1.0.0,Servo:1.2.0}}"`
