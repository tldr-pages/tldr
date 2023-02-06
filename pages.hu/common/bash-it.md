# bash-it

> Közösségi Bash parancsok és szkriptek gyűjteménye a Bash 3.2+ verzióhoz. További információ: <https://bash-it.readthedocs.io/en/latest/>.

- A Bash-it frissítése a legújabb stabil/fejlesztői verzióra:

`bash-it update {{stable|dev}}`

- Bash-profil újratöltése (az automatikus újratöltéshez állítsa a `BASH_IT_AUTOMATIC_RELOAD_AFTER_CONFIG_CHANGE` címet nem üres értékre):

`bash-it reload`

- Indítsa újra a Bash-t:

`bash-it restart`

- Bash-profil újratöltése hiba- és figyelmeztetésnaplózás engedélyezésével:

`bash-it doctor`

- A Bash-profil újratöltése hiba/riasztás/elérhetetlen naplózás engedélyezésével:

`bash-it doctor {{errors|warnings|all}}`

- Bash-it aliase-ok/pluginok/végződések keresése:

`bash-it search {{alias|plugin|completion}}`

- Bash-it aliasok/pluginok/kiegészítők keresése és az összes talált elem engedélyezése/letiltása:

`bash-it search --{{enable|disable}} {{alias|plugin|completion}}`
