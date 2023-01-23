# Measure-Command

> A parancsfájlblokkok és parancsértelmezők futtatásának idejét méri. Ez a parancs csak a PowerShell segítségével használható. További információ: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/measure-command>.

- Egy parancs futtatásához szükséges idő mérése:

`Measure-Command { {{command}} }`

- Pipe input a Measure-Command (a `Measure-Command` címre pipázott objektumok a Expression paraméterhez átadott parancsfájlblokk számára elérhetőek):

`10, 20, 50 | Measure-Command -Expression { for ($i=0; $i -lt $_; $i++) {$i} }`
