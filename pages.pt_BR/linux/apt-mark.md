# apt-mark

> Utilitário que altera as configurações dos pacotes instalados.
> Mais informações: <https://manned.org/apt-mark.8>.

- Marcar um pacote como instalado automaticamente:

`sudo apt-mark auto {{nome_do_pacote}}`

- Bloquear um pacote na sua versão atual, impedindo que ele seja atualizado:

`sudo apt-mark hold {{nome_do_pacote}}`

- Desbloquear um pacote, permitindo que ele seja atualizado:

`sudo apt-mark unhold {{nome_do_pacote}}`

- Listar os pacotes instalados manualmente:

`apt-mark showmanual`

- Listar os pacotes bloqueados:

`apt-mark showhold`
