# Sort-Object

> Az objektumok tulajdonságértékek szerinti rendezése. Ez a parancs csak a PowerShell segítségével használható. További információ: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/sort-object>.

- Az aktuális könyvtár név szerinti rendezése:

`Get-ChildItem | Sort-Object`

- Az aktuális könyvtár név szerinti rendezése lefelé haladva:

`Get-ChildItem | Sort-Object -Descending`

- Az elemek rendezése a duplikációk eltávolításával:

`"a", "b", "a" | Sort-Object -Unique`

- Az aktuális könyvtár rendezése fájlhossz szerint:

`Get-ChildItem | Sort-Object -Property Length`

- A legnagyobb memóriahasználatú folyamatok rendezése a munkakészlet (WS) mérete alapján:

`Get-Process | Sort-Object -Property WS`
