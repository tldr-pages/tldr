# Invoke-Item

> Fájlok megnyitása a megfelelő alapértelmezett programokban. Ez a parancs csak a PowerShell segítségével használható. További információ: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/invoke-item>.

- Fájl megnyitása a fájl alapértelmezett programjában:

`Invoke-Item -Path {{path/to/file}}`

- Egy könyvtáron belüli összes fájl megnyitása:

`Invoke-Item -Path {{path/to/directory/*}}`

- Egy könyvtáron belüli összes PNG fájl megnyitása:

`Invoke-Item -Path {{path/to/directory/*.png}}`

- Egy adott kulcsszót tartalmazó könyvtáron belüli összes fájl megnyitása:

`Invoke-Item -Path {{path/to/directory/*}} -Include {{*keyword*}}`

- Egy könyvtáron belüli összes fájl megnyitása, kivéve azokat, amelyek egy adott kulcsszót tartalmaznak:

`Invoke-Item -Path {{path/to/directory/*}} -Exclude {{*keyword*}}`

- Szárazpróbát végezhet annak meghatározására, hogy mely fájlok nyílnak meg egy könyvtáron belül a `Invoke-Item` oldalon keresztül:

`Invoke-Item -Path {{path/to/directory/*}} -WhatIf`
