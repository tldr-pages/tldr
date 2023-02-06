# git

> Elosztott verziókezelő rendszer. Egyes alparancsoknak, mint például a `commit`, `add`, `branch`, `checkout`, `push`, stb. saját használati dokumentációjuk van, amely a `tldr git subcommand` oldalon keresztül érhető el. További információ: <https://git-scm.com/>.

- Ellenőrizze a Git verzióját:

`git --version`

- Általános súgó megjelenítése:

`git --help`

- Súgó megjelenítése egy Git alparancshoz (például `clone`, `add`, `push`, `log`, stb.):

`git help {{subcommand}}`

- Egy Git alparancs végrehajtása:

`git {{subcommand}}`

- Git alparancs végrehajtása egy egyéni tároló gyökérútján:

`git -C {{path/to/repo}} {{subcommand}}`

- Git alparancs végrehajtása egy adott konfigurációs készlettel:

`git -c '{{config.key}}={{value}}' {{subcommand}}`
