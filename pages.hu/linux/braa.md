# braa

> Ultragyors tömeges SNMP-olvasó, amely egyszerre több hosztot is lehetővé tesz. További információ: <https://github.com/mteg/braa>.

- Az állomás SNMP-fájának bejárása nyilvános karakterlánccal, az összes OID lekérdezésével a `.1.3.6` címen:

`braa public@{{ip}}:{{.1.3.6.*}}`

- A teljes `ip_range` alhálózat lekérdezése a `system.sysLocation.0` számára:

`braa public@{{ip_range}}:{{.1.3.6.1.2.1.1.6.0}}`

- Megkísérli a `system.sysLocation.0` értékét egy adott munkacsoportra beállítani:

`braa private@{{ip}}:{{.1.3.6.1.2.1.1.6.0}}=s'{{workgroup}}'`
