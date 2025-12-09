# pacaur

> Um utilitário para Arch Linux para construir e instalar pacotes a partir do Arch User Repository.
> Mais informações: <https://github.com/rmarquis/pacaur#name>.

- Sincroniza e atualiza todos os pacotes (inclui o AUR):

`pacaur -Syu`

- Sincroniza e atualiza apenas os pacotes do AUR:

`pacaur -Syua`

- Instala um novo pacote (inclui o AUR):

`pacaur -S {{pacote}}`

- Remove um pacote e suas dependências (inclui pacotes do AUR):

`pacaur -Rs {{pacote}}`

- Pesquisa o banco de dados de pacotes para uma palavra-chave (inclui o AUR):

`pacaur -Ss {{palavra-chave}}`

- Lista todos os pacotes atualmente instalados (inclui pacotes do AUR):

`pacaur -Qs`
