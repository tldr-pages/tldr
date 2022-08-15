# csrutil

> Gerencia a configuração do System Integrity Protection (SIP).
> Mais informações: <https://ss64.com/osx/csrutil.html>.

- Exibe o status do System Integrity Protection:

`csrutil status`

- Desabilita o System Integrity Protection:

`csrutil disable`

- Habilita o System Integrity Protection:

`csrutil enable`

- Exibe a lista de origens permitidas do NetBoot:

`csrutil netboot list`

- Adiciona um endereço IPv4 à lista de origens permitidas do NetBoot:

`csrutil netboot add {{endereço_ip}}`

- Reseta o status do System Integrity Protection e limpa a lista do NetBoot:

`csrutil clear`
