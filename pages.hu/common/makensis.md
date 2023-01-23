# makensis

> Cross-platform fordítóprogram NSIS telepítőkhöz, amely egy NSIS szkriptet Windows telepítő programba fordít. További információ: <https://nsis.sourceforge.io/Docs/Chapter3.html>.

- NSIS-szkript fordítása:

`makensis {{path/to/file.nsi}}`

- NSIS-szkriptet fordít szigorú módban (a figyelmeztetéseket hibaként kezeli):

`makensis -WX {{path/to/file.nsi}}`

- Súgó nyomtatása egy adott parancshoz:

`makensis -CMDHELP {{command}}`
