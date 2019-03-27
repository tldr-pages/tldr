# apt-mark

> Utilitário que altera as configurações dos pacotes instalados.

- Marca um pacote como instalado automaticamente:

`sudo apt-mark auto {{package_name}}`

- Trava um pacote na sua versão atual impedindo que ele seja atualizado.:

`sudo apt-mark hold {{package_name}}`

- Permite que um pacote seja atualizado novamente:

`sudo apt-mark unhold {{package_name}}`

- Lista os pacotes instalado manualmente:

`apt-mark showmanual`

- Lista os pacotes que estão travados e não podem ser atualizados:

`apt-mark showhold`
