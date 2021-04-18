# age

> Ein einfaches, modernes und sicheres Dateiverschlüsselungswerkzeug.
> Mehr Informationen: <https://age-encryption.org>.

- Generiere eine verschlüsselte Datei, die mit einer Passphrase entschlüsselt werden kann:

`age --passphrase --output {{pfad/zu/verschlüsselter_datei}} {{pfad/zu/unverschlüsselter_datei}}`

- Generiere ein Schlüsselpaar, speichere dabei den öffentlichen und privaten Schlüssel in einer unverschlüsselten Schlüsseldatei und gib den öffentlichen Schlüssel zu stdout aus:

`age-keygen --output {{pfad/zu/schlüsseldatei}}`

- Verschlüssle eine Datei zu einem oder mehreren öffentlichen Schlüsseln, die als Zeichenketten eingegeben werden:

`age --output {{pfad/zu/verschlüsselter_datei}} --recipient {{öffentlicher_schlüssel_1}} --recipient {{öffentlicher_schlüssel_2}} {{pfad/zu/unverschlüsselter_datei}}`

- Verschlüssle eine Datei zu einem oder mehreren öffentlichen Schlüsseln, die in einer Empfängerdatei angegeben sind:

`age --output {{pfad/zu/verschlüsselter_datei}} --recipients-file {{pfad/zu/empfängerdatei}} {{pfad/zu/unverschlüsselter_datei}}`

- Entschlüssle eine Datei mit einer Passphrase:

`age --decrypt --output {{pfad/zu/entschlüsselter_datei}} {{pfad/zu/verschlüsselter_datei}}`

- Entschlüssle eine Datei mit einer privaten Schlüsseldatei:

`age --decrypt --identity {{pfad/zu/privater_schlüsseldatei}} --output {{pfad/zu/entschlüsselter_datei}} {{pfad/zu/verschlüsselter_datei}}`
