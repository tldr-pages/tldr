# zypper

> Utilitário de gerenciamento de pacotes SUSE e openSUSE.
> Mais informações: <https://en.opensuse.org/SDB:Zypper_manual>.

- Sincroniza a lista de pacotes e versões disponíveis:

`sudo zypper {{[ref|refresh]}}`

- Instala um novo pacote:

`sudo zypper {{[in|install]}} {{pacote}}`

- Remove um pacote:

`sudo zypper {{[rm|remove]}} {{pacote}}`

- Atualiza os pacotes instalados para as versões mais recentes disponíveis:

`sudo zypper {{[up|update]}}`

- Pesquisa pacote por palavra-chave:

`zypper {{[se|search]}} {{palavra-chave}}`

- Mostra informações relacionadas aos repositórios configurados:

`zypper {{[lr|repos]}} --sort-by-priority`
