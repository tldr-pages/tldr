# sudo

> Executa um único comando como o Superuser, ou como outro usuário.
> Mais informações: <https://www.sudo.ws/sudo.html>.

- Executa um comando como Superuser:

`sudo {{less /var/log/syslog}}`

- Edita um arquivo, como Superuser, com seu editor padrão:

`sudo --edit {{/etc/fstab}}`

- Executa um comando como outro usuário e/ou grupo:

`sudo --user={{usuário}} --group={{grupo}} {{id -a}}`

- Executa um comando anterior com o prefixo `sudo` (apenas em Bash, Zsh, etc.):

`sudo !!`

- Abre o shell padrão com privilégios de Superuser e executa arquivos de login (`.profile`, `.bash_profile`, etc.):

`sudo --login`

- Abre o shell padrão com privilégios de Superuser sem altera o ambiente de execução:

`sudo --shell`

- Abre o shell padrão como dado usuário, carregando o ambiente de execução deste usuário e lendo arquivos de login (`.profile`, `.bash_profile`, etc.):

`sudo --login --user={{usuário}}`

- Lista os comandos permitidos (e não permitidos) para o usuário atual:

`sudo --list`
