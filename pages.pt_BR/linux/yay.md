# yay

> Yet Another Yogurt: Um utilitário de Arch Linux para compilar e instalar pacotes do AUR (Arch User Repository).
> Veja também `pacman`.
> Mais informações: <https://github.com/Jguer/yay>.

- Busca interativamente e instala pacotes dos repositórios e AUR:

`yay {{nome_do_pacote|termo_de_busca}}`

- Sincroniza e atualiza todos os pacotes dos repositórios e AUR:

`yay`

- Sincroniza e atualiza apenas pacotes AUR:

`yay -Sua`

- Instala um novo pacote de repositório e AUR:

`yay -S {{nome_do_pacote}}`

- Remove um pacote instalado, suas dependências e arquivos de configuração:

`yay -Rns {{nome_do_pacote}}`

- Procura no banco de dados de pacotes por uma palavra-chave dos repositórios e AUR:

`yay -Ss {{palavra_chave}}`

- Remove pacotes órfãos (instalado como dependência mas não utilizado por qualquer pacote):

`yay -Yc`

- Mostra estatísticas dos pacotes instalados e condição do sistema:

`yay -Ps`
