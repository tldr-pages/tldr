# Select-String

> Szöveg keresése karakterláncokban és fájlokban a PowerShellben. Ezt a parancsot csak a PowerShell segítségével lehet használni. A `Select-String` parancsot a UNIX-ban a grep-hez hasonlóan használhatja, vagy a findstr.exe-t a Windowsban. További információ: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/select-string>.

- Egy fájlban lévő minta keresése:

`Select-String -Path "{{path/to/file}}" -Pattern '{{search_pattern}}'`

- Pontos karakterlánc keresése (kikapcsolja a reguláris kifejezéseket):

`Select-String -SimpleMatch "{{exact_string}}" {{path/to/file}}`

- Keresés a mintára az aktuális dir összes `.ext` fájljában:

`Select-String -Path "{{*.ext}}" -Pattern '{{search_pattern}}'`

- A mintának megfelelő sor előtt és után megadott számú sor rögzítése:

`Select-String --Context {{2,3}} "{{search_pattern}}" {{path/to/file}}`

- A mintának nem megfelelő sorok keresése az stdin-ben:

`Get-Content {{path/to/file}} | Select-String --NotMatch "{{search_pattern}}"`
