# apt-mark

> Utilitário que altera as configurações dos pacotes instalados.
> Mais informações: <https://manned.org/apt-mark>.

- Marca um pacote como instalado automaticamente:

`sudo apt-mark auto {{pacote}}`

- Bloqueia um pacote na sua versão atual, impedindo que ele seja atualizado:

`sudo apt-mark hold {{pacote}}`

- Desbloqueia um pacote, permitindo que ele seja atualizado:

`sudo apt-mark unhold {{pacote}}`

- Lista os pacotes instalados manualmente:

`apt-mark showmanual`

- Lista os pacotes bloqueados:

`apt-mark showhold`
