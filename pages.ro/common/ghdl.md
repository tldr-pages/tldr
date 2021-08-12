# ghdl

> Simulator open-source pentru limba VHDL.
> Mai multe informaţii: <http://ghdl.free.fr>

- Analizați un fișier sursă VHDL și produceți un fișier obiect:

`ghdl -a {{filename.vhdl}}`

- Elaborarea unui proiect (unde `{design}}` este numele unei unități de configurare, al unei unități de entitate sau al unei unități de arhitectură):

`ghdl -e {{design}}`

- Rulați un design elaborat:

`ghdl -r {{design}}`

- Rulați un proiect elaborat și dump ieșire la un fișier formă de undă:

`ghdl -r {{design}} --wave={{output.ghw}}`

- Verificați sintaxa unui fișier sursă VHDL:

`ghdl -s {{filename.vhdl}}`

- Afișează pagina de ajutor:

`ghdl --help`
