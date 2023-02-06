# solo

> Kölcsönhatás a Solo hardveres biztonsági kulcsokkal. További információ: <https://github.com/solokeys/solo-python>.

- Csatlakoztatott Solók listája:

`solo ls`

- Az aktuálisan csatlakoztatott Solo firmware-jének frissítése a legújabb verzióra:

`solo key update`

- Egy adott Solo LED-jének villogtatása:

`solo key wink --serial {{serial_number}}`

- Véletlenszerű bájtok generálása az aktuálisan csatlakoztatott Solo biztonságos véletlenszám-generátorával:

`solo key rng raw`

- Egy Solo soros kimenetének figyelése:

`solo monitor {{path/to/serial_port}}`
