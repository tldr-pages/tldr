# command

> Comanda forțează shell-ul să execute programul și să ignore orice funcții, builtins și aliasuri cu același nume.
> Mai multe informaţii: <https://manned.org/command>

- Executa programul `ls` literalmente, chiar daca exista un alias `ls`:

`command {{ls}}`

- Afișați calea către executabil sau definiția alias a unei anumite comenzi:

`command -v {{command_name}}`
