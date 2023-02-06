# influx

> InfluxDB parancssori kliens. További információ: <https://docs.influxdata.com/influxdb/v1.7/tools/shell/>.

- Csatlakozás a localhost-on futó InfluxDB-hez hitelesítő adatok nélkül:

`influx`

- Csatlakozás egy adott felhasználónévvel (jelszót fog kérni):

`influx -username {{username}} -password ""`

- Csatlakozás egy adott állomáshoz:

`influx -host {{hostname}}`

- Egy adott adatbázis használata:

`influx -database {{database_name}}`

- Egy adott parancs végrehajtása:

`influx -execute "{{influxql_command}}"`

- Kimenet visszaadása egy adott formátumban:

`influx -execute "{{influxql_command}}" -format {{json|csv|column}}`
