# findfs

> Găsește un sistem de fișiere după etichetă sau UUID.
> Mai multe informaţii: <https://mirrors.edge.kernel.org/pub/linux/utils/util-linux>

- Căutare dispozitive bloc după eticheta sistemului de fișiere:

`findfs LABEL={{label}}`

- Căutare după sistemul de fișiere UUID:

`findfs UUID={{uuid}}`

- Căutare după eticheta de partiție (tabelul de partiții GPT sau MAC):

`findfs PARTLABEL={{partition_label}}`

- Căutare după partiția UUID (numai tabela de partiții GPT):

`findfs PARTUUID={{partition_uuid}}`
