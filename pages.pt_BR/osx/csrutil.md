# csrutil

> Gerenciar a configuração do System Integrity Protection (SIP).
> Mais informações: <https://ss64.com/osx/csrutil.html>.

- Exibir o status do System Integrity Protection:

`csrutil status`

- Desabilitar o System Integrity Protection:

`csrutil disable`

- Habilitar o System Integrity Protection:

`csrutil enable`

- Exibir a lista de origens permitidas do NetBoot:

`csrutil netboot list`

- Adicionar um endereço IPv4 à lista de origens permitidas do NetBoot:

`csrutil netboot add {{endereço_ip}}`

- Resetar o status do System Integrity Protection e limpar a lista do NetBoot:

`csrutil clear`
