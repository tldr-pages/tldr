# mailx

> Levelek küldése és fogadása. További információ: <https://manned.org/mailx>.

- Levél küldése (a tartalmat a parancs után kell beírni, és a `Ctrl+D` végződéssel kell befejezni):

`mailx -s "{{subject}}" {{to_addr}}`

- Levél küldése egy másik parancsból átadott tartalommal:

`echo "{{content}}" | mailx -s "{{subject}}" {{to_addr}}`

- Levél küldése fájlból beolvasott tartalommal:

`mailx -s "{{subject}}" {{to_addr}} < {{content.txt}}`

- Levél küldése egy címzettnek és CC egy másik címre:

`mailx -s "{{subject}}" -c {{cc_addr}} {{to_addr}}`

- Levél küldése a feladó címének megadásával:

`mailx -s "{{subject}}" -r {{from_addr}} {{to_addr}}`

- Levél küldése csatolmánnyal:

`mailx -a {{path/to/file}} -s "{{subject}}" {{to_addr}}`
