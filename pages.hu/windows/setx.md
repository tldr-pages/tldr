# setx

> Állandó környezeti változók beállítása. További információ: <https://learn.microsoft.com/windows-server/administration/windows-commands/setx>.

- Környezeti változó beállítása az aktuális felhasználó számára:

`setx {{variable}} {{value}}`

- Környezeti változó beállítása az aktuális géphez:

`setx {{variable}} {{value}} /M`

- Környezeti változó beállítása egy távoli gépen lévő felhasználó számára:

`setx /s {{hostname}} /u {{username}} /p {{password}} {{variable}} {{value}}`

- Környezeti változó beállítása egy beállításjegyzékkulcs értékéből:

`setx {{variable}} /k {{registry\key\path}}`
