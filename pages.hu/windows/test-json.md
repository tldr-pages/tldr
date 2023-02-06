# Test-Json

> Megvizsgálja, hogy egy karakterlánc érvényes JSON dokumentum-e. Ez a parancs csak a PowerShell segítségével használható. További információ: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/test-json>.

- Annak tesztelése, hogy egy stdin-ből érkező karakterlánc JSON formátumú-e:

`'{{string}}' | Test-Json`

- Annak tesztelése, hogy egy karakterlánc JSON formátumú-e:

`Test-Json -Json '{{json_to_test}}'`

- Annak tesztelése, hogy az stdin-ből érkező karakterlánc megfelel-e egy adott sémafájlnak:

`'{{string}}' | Test-Json -SchemaFile {{path/to/schema.json}}`
