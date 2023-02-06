# Out-String

> A bemeneti objektumok stringként történő kiadása. Ez a parancs csak a PowerShell segítségével használható. További információ: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/out-string>.

- A hosztinformációk stringként történő kiírása:

`Get-Alias | Out-String`

- Minden objektumot karakterlánccá alakít, ahelyett, hogy az összes objektumot egyetlen karakterlánccá fűzné össze:

`Get-Alias | Out-String -Stream`

- Használja a `Width` paramétert a csonkítás megakadályozásához:

`@{TestKey = ('x' * 200)} | Out-String -Width {{250}}`
