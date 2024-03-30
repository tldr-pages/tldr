# age

> Ein einfaches, modernes und sicheres Dateiverschlüsselungswerkzeug.
> Weitere Informationen: <https://github.com/FiloSottile/age>.

- Generiere eine verschlüsselte Datei, die mit einer Passphrase entschlüsselt werden kann:

`age --passphrase --output {{pfad/zu/verschlüsselter_datei}} {{pfad/zu/unverschlüsselter_datei}}`

- Generiere ein Schlüsselpaar, speichere dabei den privaten Schlüssel in einer unverschlüsselten Datei und gib den öffentlichen Schlüssel zu `stdout` aus:

`age-keygen --output {{pfad/zu/datei}}`

- Verschlüssle eine Datei mit einem oder mehr öffentlichen Schlüsseln, die als Zeichenketten eingegeben werden:

`age --recipient {{öffentlicher_schlüssel_1}} --recipient {{öffentlicher_schlüssel_2}} {{pfad/zu/unverschlüsselter_datei}} --output {{pfad/zu/verschlüsselter_datei}}`

- Verschlüssle eine Datei mit einem oder mehr öffentlichen Schlüsseln, die in einer Empfängerdatei angegeben sind:

`age --recipients-file {{pfad/zu/empfängerdatei}} {{pfad/zu/unverschlüsselter_datei}} --output {{pfad/zu/verschlüsselter_datei}}`

- Entschlüssle eine Datei mit einer Passphrase:

`age --decrypt --output {{pfad/zu/entschlüsselter_datei}} {{pfad/zu/verschlüsselter_datei}}`

- Entschlüssle eine Datei mit einer privaten Schlüsseldatei:

`age --decrypt --identity {{pfad/zu/privater_schlüsseldatei}} --output {{pfad/zu/entschlüsselter_datei}} {{pfad/zu/verschlüsselter_datei}}`
