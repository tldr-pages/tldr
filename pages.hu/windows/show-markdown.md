# Show-Markdown

> Markdown fájl vagy karakterlánc megjelenítése a konzolon barátságos módon, VT100 escape szekvenciák használatával, vagy böngészőben HTML használatával. Ez a parancs csak a PowerShell segítségével használható. További információ: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/show-markdown>.

- Markdown megjelenítése konzolra egy fájlból:

`Show-Markdown -Path {{path/to/file}}`

- Markdown konzolra történő megjelenítése karakterláncból:

`{{"# Markdown content"}} | Show-Markdown`

- Markdown fájl megnyitása böngészőben:

`Show-Markdown -Path {{path/to/file}} -UseBrowser`
