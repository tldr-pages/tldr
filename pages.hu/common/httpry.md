# httpry

> Könnyű csomagkereső a HTTP forgalom megjelenítésére és naplózására. Futtatható valós időben, a forgalom elemzése közben megjelenítve azt, vagy egy démon folyamatként, amely egy kimeneti fájlba naplóz. További információ: <http://dumpsterventures.com/jason/httpry/>.

- Kimenet mentése egy fájlba:

`httpry -o {{path/to/file.log}}`

- Figyeljen egy adott interfészre, és mentse a kimenetet egy bináris pcap formátumú fájlba:

`httpry {{eth0}} -b {{path/to/file.pcap}}`

- A kimenet szűrése a HTTP igék vesszővel elválasztott listája alapján:

`httpry -m {{get|post|put|head|options|delete|trace|connect|patch}}`

- Olvasás egy bemeneti rögzítőfájlból és szűrés IP szerint:

`httpry -r {{path/to/file.log}} '{{host 192.168.5.25}}'`

- Futtatás démonfolyamatként:

`httpry -d -o {{path/to/file.log}}`
