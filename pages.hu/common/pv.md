# pv

> Az adatok haladásának nyomon követése egy csövön keresztül. További információ: <https://manned.org/pv>.

- A fájl tartalmának kinyomtatása és egy előrehaladási sáv megjelenítése:

`pv {{path/to/file}}`

- A csövek közötti adatáramlás sebességének és mennyiségének mérése (`--size` opcionális):

`command1 | pv --size {{expected_amount_of_data_for_eta}} | command2`

- Egy fájl szűrése, a haladás és a kimeneti adatok mennyiségének megtekintése:

`pv -cN in {{big_text_file}} | grep {{pattern}} | pv -cN out > {{filtered_file}}`

- Csatlakozás egy már futó folyamathoz, és a fájlolvasás előrehaladásának megtekintése:

`pv -d {{PID}}`

- Hibás fájl beolvasása, a hibák kihagyása, mint a `dd conv=sync,noerror`:

`pv -EE {{path/to/faulty_media}} > image.img`

- Az olvasás leállítása a megadott adatmennyiség beolvasása után, sebességkorlátozás 1K/s-ra:

`pv -L 1K --stop-at --size {{maximum_file_size_to_be_read}}`
