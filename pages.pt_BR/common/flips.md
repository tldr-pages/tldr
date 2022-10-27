# flips

> Cria e aplica patches em arquivos IPS e BPS.
> Mais informações: <https://github.com/Alcaro/Flips>.

- Abre Flips para criar e aplicar um patch:

`flips`

- Aplica um patch criando um novo arquivo ROM:

`flips --apply {{patch.bps}} {{rom.smc}} {{hack.smc}}`

- Cria um patch a partir de duas ROMs:

`flips --create {{rom.smc}} {{hack.smc}} {{patch.bps}}`
