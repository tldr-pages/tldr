# influx

> Client de linie de comandă InfluxDB.
> Mai multe informaţii: <https://docs.influxdata.com/influxdb/v1.7/tools/shell/>

- Conectați-vă la un InfluxDB care rulează pe localhost fără acreditări:

`influx`

- Conectați-vă cu un anumit nume de utilizator (va solicita o parolă):

`influx -username {{username}} -password ""`

- Conectați-vă la o anumită gazdă:

`influx -host {{hostname}}`

- Utilizați o bază de date specifică:

`influx -database {{database_name}}`

- Execută o comandă dată:

`influx -execute "{{influxql_command}}"`

- Returnați ieșirea într-un format specific:

`influx -execute "{{influxql_command}}" -format {{json|csv|column}}`
