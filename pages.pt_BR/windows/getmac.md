# Getmac

> Exibe os endereços MAC de um sistema.
> Mais informações: https://learn.microsoft.com/windows-server/administration/windows-commands/getmac .

- Exibir os endereços MAC do sistema atual:
getmac

- Exibir os detalhes em um formato específico:
getmac /fo {{table|list|csv}}

- Excluir o cabeçalho na lista de saída:
getmac /nh

- Exibir os endereços MAC de uma máquina remota:
getmac /s {{hostname}} /u {{username}} /p {{password}}

- Exibir os endereços MAC com informações detalhadas:
getmac /v

- Ajuda de exibição:
getmac /?
