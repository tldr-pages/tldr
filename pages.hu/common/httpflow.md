# httpflow

> Parancssori segédprogram a HTTP-adatfolyamok rögzítésére és kiürítésére. További információ: <https://github.com/six-ddc/httpflow>.

- Az összes interfész forgalmának rögzítése:

`httpflow -i {{any}}`

- Használjon bpf-stílusú rögzítést az eredmények szűréséhez:

`httpflow {{host httpbin.org or host baidu.com}}`

- Használjon reguláris kifejezést a kérések URL-címek szerinti szűréséhez:

`httpflow -u '{{regular_expression}}'`

- Csomagok olvasása pcap formátumú bináris fájlból:

`httpflow -r {{out.cap}}`

- A kimenet kiírása egy könyvtárba:

`httpflow -w {{path/to/directory}}`
