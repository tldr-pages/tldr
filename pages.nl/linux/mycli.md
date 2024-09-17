# mycli

> Een CLI voor MySQL, MariaDB en Percona met automatische aanvulling en syntaxisaccentuering.
> Meer informatie: <https://manned.org/mycli>.

- Verbinden met een database met de huidige ingelogde gebruiker:

`mycli {{database_naam}}`

- Verbinden met een database met de opgegeven gebruiker:

`mycli -u {{gebruiker}} {{database_naam}}`

- Verbinden met een database op de opgegeven host met de opgegeven gebruiker:

`mycli -u {{gebruiker}} -h {{host}} {{database_naam}}`
