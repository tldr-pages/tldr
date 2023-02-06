# eventcreate

> Egyéni bejegyzések létrehozása az eseménynaplóban. Az eseményazonosítók 1 és 1000 közötti számok lehetnek. További információ: <https://learn.microsoft.com/windows-server/administration/windows-commands/eventcreate>.

- Új esemény létrehozása egy adott azonosítóval (1-1000) a naplóban:

`eventcreate /t {{success|error|warning|information}} /id {{id}} /d "{{message}}"`

- Esemény létrehozása egy adott eseménynaplóban:

`eventcreate /l {{log_name}} /t {{type}} /id {{id}} /d "{{message}}"`

- Esemény létrehozása egy adott forrással:

`eventcreate /so {{source_name}} /t {{type}} /id {{id}} /d "{{message}}"`

- Esemény létrehozása egy távoli gép eseménynaplójában:

`eventcreate /s {{hostname}} /u {{username}} /p {{password}} /t {{type}} /id {{id}} /d "{{message}}"`
