# Diskpart

> Gerenciador de disco, volume e partição.
> Mais informações: https://learn.microsoft.com/windows-server/administration/windows-commands/diskpart .

- Executa o diskpart sozinho em um prompt de comando administrativo para entrar na linha de comando:
diskpart

- Lista todos os discos:
list disk

- Seleciona um volume:
select volume {{volume}}

- Atribua uma letra de unidade ao volume selecionado:
assign letter {{letter}}

- Crie uma nova partição:
create partition primary

- Ative o volume selecionado:
active

- Sair do diskpart:
exit
