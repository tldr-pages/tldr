# curl

> No PowerShell, este comando pode ser um apelido de `Invoke-WebRequest` quando o programa `curl` original (<https://curl.se>) não está adequadamente instalado.
> Mais informações: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/invoke-webrequest>.

- Exibe documentação sobre o comando `curl` original:

`tldr curl -p common`

- Exibe documentação sobre o comando `Invoke-WebRequest` do PowerShell:

`tldr invoke-webrequest`

- Verifica se `curl` está instalado corretamente imprimindo seu número de versão. Se esse comando for avaliado como um erro, o PowerShell pode ter substituído esse comando por `Invoke-WebRequest`:

`curl --version`
