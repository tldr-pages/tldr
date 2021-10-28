# yaourt

> Utilitário de Arch Linux para compilaçào de pacotes AUR (Arch User Repository).
> Mais informações: <https://linuxcommandlibrary.com/man/yaourt>.

- Sincroniza e atualiza todos os pacotes (incluindo AUR):

`yaourt -Syua`

- Instala um novo pacote (incluindo AUR):

`yaourt -S {{nome_do_pacote}}`

- Remove um pacote e suas dependências (incluindo pacotes AUR):

`yaourt -Rs {{nome_do_pacote}}`

- Procura no banco de dados de pacotes por uma palavra-chave (incluindo AUR):

`yaourt -Ss {{nome_do_pacote}}`

- Lista pacotes instalados, versões, e repositórios (pacotes AUR serão listados sob como repositório 'local'):

`yaourt -Q`
