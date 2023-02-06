# rtl_sdr

> Nyers adatrögzítő RTL-SDR vevőkhöz. Az adatok kódolása I/Q mintavételezéssel (más néven kvadratúra mintavételezéssel) történik. További információ: <https://osmocom.org/projects/rtl-sdr/wiki/Rtl-sdr>.

- A RAW-adatok mentése egy (Hz-ben megadott) frekvenciáról egy fájlba:

`rtl_sdr -f {{100000000}} {{path/to/file}}`

- Az adatok átvezetése egy másik programba:

`rtl_sdr -f {{100000000}} - | {{aplay}}`

- Meghatározott számú minta beolvasása:

`rtl_sdr -f {{100000000}} -n {{20}} -`

- A mintavételi frekvencia megadása Hz-ben (225001-300000 és 900001-3200000 tartományok):

`rtl_sdr -f {{100000000}} -s {{2400000}} -`

- Az eszköz megadása az indexével:

`rtl_sdr -f {{100000000}} -d {{0}} -`

- Az erősítés megadása:

`rtl_sdr -f {{100000000}} -g {{20}} -`

- A kimeneti blokk méretének megadása:

`rtl_sdr -f {{100000000}} -b {{9999999}} -`

- Szinkron kimenet használata:

`rtl_sdr -f {{100000000}} -S -`
